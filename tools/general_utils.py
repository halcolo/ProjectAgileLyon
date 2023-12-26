from tools.db_utils import response_message
from tools.db_utils import db_get_doc, db_set_doc, db_get_doc
import statistics
import logging


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
        # Check if the player exists in the game
        if player_id in players.keys():
            players[player_id] = score
        
        game["players"] = players
            
        # Getting the players that have not yet scored game
        players_scored = [int(s) for s in players.values() if int(s) == 0]
        
        # If all players have scored, calculate the final score
        if len(players_scored) == 0 and game.get("final_score") == 0:
            new_score, type_res =  calculate_result(
                    game_mode=int(game.get('game_mode')),
                    players=players)
            # Setting up the final score and game mode
            game["final_score"] = new_score
            game["game_mode"] = type_res

        db_set_doc(
            collection_name=collection, 
            doc_id=task_id, 
            data=game
            )
        return response_message(f"Player {player_id} added to game {task_id}")
    except Exception as e:
        return response_message(
            f"An error occurred while adding player {player_id} to game {task_id}: {e}",
            500,
        )
     
def check_score(func):
    def wrapper(*args, **kwargs):
        score, type_res = func(*args, **kwargs)
        if score is not None and isinstance(int(score), int):
            return int(score), type_res  
        else:
            return 0
    return wrapper


def get_modes():
    game_types = db_get_doc("dicts", "modes")
    return game_types

def get_mode_string(mode):
    game_modes = get_modes()
    try:
        for k, v in game_modes.items():
            if int(v) == int(mode):
                return  k
        return None
    except Exception as e:
        logging.error(f"An error occurred while getting the game mode: {e}")
        return None
    
@check_score
def calculate_result(game_mode, players) -> tuple :
    result = None
    game_mode_str = get_mode_string(game_mode)
    try:
        if game_mode_str is not None:
            game_mode_str = game_mode_str.lower()
            all_scores = [int(s) for s in players.values() if isinstance(int(s), int)]
            if len(set(all_scores)) == 1:
                result = all_scores[0]
                game_mode_str = "Unanimity"
                print(f"Unanimity result: {result}")
            if game_mode_str == "Average".lower():
                result = sum(all_scores) / len(all_scores)
                print(f"Average result: {result}")
            elif game_mode_str == "Median".lower():
                result = statistics.median(all_scores)
                print(f"Median result: {result}")
            elif game_mode_str == "Majority".lower():
                result = max(set(all_scores))
                print(f"Majority result: {result}")
        return result, game_mode_str
    except Exception as e:
        logging.error(f"An error occurred while calculating the result: {e}")
        return result, game_mode_str

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
       