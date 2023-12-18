from config import db
from flask import jsonify
import secrets


def response(message: str, status_code: int = 200):
    """
    Creates a JSON response with the given message and status code.

    Args:
        message (str): The message to include in the response.
        status_code (int, optional): The HTTP status code. Defaults to 200.

    Returns:
        tuple: A tuple containing the JSON response and the status code.
    """
    resp = {"code": status_code, "message": message}
    return jsonify(resp), status_code


def db_create_doc(collection_name: str, data: dict, auto_id: bool = True):
    """
    Create a new document in the specified collection.

    Args:
        collection_name (str): The name of the collection to create the document in.
        data (dict): The data to be added to the document.
        auto_id (bool, optional): Whether to automatically generate an ID for the document.
            Defaults to True.

    Returns:
        str: A response message indicating the success or failure of the operation.
    """
    try:
        if auto_id:
            db.collection(collection_name).add(data)
        else:
            db.collection(collection_name).document(data["id"]).set(data)
        return response(
            f"Document created successfully in collection {collection_name}"
        )
    except Exception as e:
        return response(f"An error occurred while crating the document: {e}", 500)


def db_add_player_2_task(player_id: str, task_id: str):
    try:
        game = db.collection("task").document(task_id).get().to_dict()
        players = game["players"]
        players[player_id] = 0
        game["players"] = players
        db.collection("task").document(task_id).set(game)
        return response(f"Player {player_id} added to game {task_id}")
    except Exception as e:
        return response(
            f"An error occurred while adding player {player_id} to game {task_id}: {e}",
            500,
        )

def update_task_points(player_id:str,
                       task_id:str, 
                       score:str, 
                       collection:str="task"):
    try:
        game = db.collection(collection).document(task_id).get().to_dict()
        players = game["players"]
        if player_id in players.keys():
            players[player_id] = score
        game["players"] = players
        db.collection(collection).document(task_id).set(game)
        return response(f"Player {player_id} added to game {task_id}")
    except Exception as e:
        return response(
            f"An error occurred while adding player {player_id} to game {task_id}: {e}",
            500,
        )

def evaluate_task(
    task_id: str, collection: str = "task", game_mode: str = "fibbo_13"
):
    try:
        game = db.collection(collection).document(task_id).get().to_dict()
        players = game["players"]
        scores = [int(score) for score in players.values()]
        final_score = 0
        if game_mode == "fibbo_13":
            final_score = fibbo_13(scores)
        game["final_score"] = final_score
        db.collection(collection).document(task_id).set(game)
        return response(f"Game {task_id} evaluated successfully")
    except Exception as e:
        return response(f"An error occurred while evaluating game {task_id}: {e}", 500)
    
def reveal_estimates(self):
    for player in self.players:
        print(f"{player.name}'s estimate: {player.estimate}")

def calculate_result(self):
    if self.mode == None:
        self.select_modes()
    estimates = [player.estimate for player in self.players]
    if self.mode == "Unanimity":
        if len(set(estimates)) == 1:
            print(f"Unanimity result: {estimates[0]}")
        else:
            print("No unanimity")
    elif self.mode == "Average":
        print(f"Average result: {sum(estimates) / len(estimates)}")
    elif self.mode == "Median":
        print(f"Median result: {statistics.median(estimates)}")
    elif self.mode == "Majority":
        print(f"Majority result: {max(set(estimates), key=estimates.count)}")
