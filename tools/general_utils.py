import secrets
from config import db
from tools.db_utils import response_message
from tools.db_utils import db_get_doc, db_set_doc
import statistics


def update_task_points(player_id:str,
                       task_id:str, 
                       score:str, 
                       collection:str="task"):
    try:
        # task = Task(id=task_id)
        game = db_get_doc(
            collection_name=collection, 
            doc_id=task_id
            )
        players = game["players"]
        players_scored = [int(s) for s in players.values() if int(s) == 0]
        if game.get("final_score") == 0:
            if players_scored == []:
                new_score = calculate_result(
                    game_mode=int(game.get('game_mode')),
                    players=players)
                game["final_score"] = new_score
            if player_id in players.keys():
                players[player_id] = score
            game["players"] = players
            db_set_doc(
                collection_name=collection, 
                doc_id=task_id, 
                data=game
                )
            return response_message(f"Player {player_id} added to game {task_id}")
        return response_message(f"Game {task_id} already evaluated")
    except Exception as e:
        return response_message(
            f"An error occurred while adding player {player_id} to game {task_id}: {e}",
            500,
        )
     
def check_score(func):
    def wrapper(*args, **kwargs):
        score = func(*args, **kwargs)
        if score is not None and isinstance(score, int):
            return score
        else:
            return 0
    return wrapper


def select_modes(game_mode=int):
    game_types = db.collection("dicts").document("modes").get().to_dict().items()
    for game in game_types:
        if int(game[1]) == int(game_mode):
            return game[0]


@check_score
def calculate_result(game_mode, players):
    game_mode_str = select_modes(game_mode)
    game_mode_str = game_mode_str.lower()
    all_scores = [int(s) for s in players.values() if isinstance(s, int)]
    if game_mode_str == "Average".lower():
        print(f"Average result: {sum(all_scores) / len(all_scores)}")
        return sum(all_scores) / len(all_scores)
    elif game_mode_str == "Median".lower():
        print(f"Median result: {statistics.median(all_scores)}")
        return statistics.median(all_scores)
    elif game_mode_str == "Majority".lower():
        print(f"Majority result: {max(set(all_scores))}")
        return max(set(all_scores))
    elif game_mode_str == "Unanimity".lower():
        if len(set(all_scores)) == 1:
            print(f"Unanimity result: {all_scores[0]}")
            return all_scores[0]
        else:
            print("No unanimity")
            
    return None

# def evaluate_task(
#     task_id: str, collection: str = "task", game_mode: str = "fibbo_13"
# ):
#     try:
#         game = db.collection(collection).document(task_id).get().to_dict()
#         players = game["players"]
#         scores = [int(score) for score in players.values()]
#         final_score = 0
#         if game_mode == "fibbo_13":
#             final_score = fibbo_13(scores)
#         game["final_score"] = final_score
#         db.collection(collection).document(task_id).set(game)
#         return response(f"Game {task_id} evaluated successfully")
#     except Exception as e:
#         return response(f"An error occurred while evaluating game {task_id}: {e}", 500)
       