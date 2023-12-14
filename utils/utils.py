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


def db_add_player_2_task(player_id: str, game_code: str):
    try:
        game = db.collection("task").document(game_code).get().to_dict()
        players = game["players"]
        players[player_id] = 0
        game["players"] = players
        db.collection("task").document(game_code).set(game)
        return response(f"Player {player_id} added to game {game_code}")
    except Exception as e:
        return response(
            f"An error occurred while adding player {player_id} to game {game_code}: {e}",
            500,
        )
