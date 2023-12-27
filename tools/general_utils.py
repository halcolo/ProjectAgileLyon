from tools.db_utils import response_message
from tools.db_utils import db_get_doc, db_set_doc, db_get_doc
import statistics
import logging


def update_task_points(player_id:str,
                       task_id:str, 
                       score:str, 
                       collection:str="task"):
    """
    Updates the points of a player in a game task.

    Args:
        player_id (str): The ID of the player.
        task_id (str): The ID of the game task.
        score (str): The new score of the player.
        collection (str, optional): The name of the collection. Defaults to "task".

    Returns:
        str: A response message indicating the success or failure of the operation.
    """
    try:
        # task = Task(id=task_id)
        game = db_get_doc(
            collection_name=collection, 
            doc_id=task_id
            )
        players = game["players"]
        # Check if the player exists in the game
        if player_id in players.keys() and int(players[player_id]) == 0:
            players[player_id] = score
            
            if len(players) > 1:
        
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
    """
    Decorator function that checks the score returned by the decorated function.
    
    Args:
        func: The function to be decorated.
    
    Returns:
        A wrapper function that checks the score returned by the decorated function.
        If the score is not None and is an integer, it is returned along with the type_res.
        Otherwise, 0 is returned.
    """
    def wrapper(*args, **kwargs):
        score, type_res = func(*args, **kwargs)
        if score is not None and isinstance(int(score), int):
            return int(score), type_res  
        else:
            return 0
    return wrapper


def get_modes():
    """
    Retrieve the available game modes from the database.

    Returns:
        dict: A dictionary containing the game modes.
    """
    game_types = db_get_doc("dicts", "modes")
    return game_types

def get_mode_string(mode):
    """
    Returns the game mode string corresponding to the given mode.

    Args:
        mode (int): The mode value to retrieve the string for.

    Returns:
        str or None: The game mode string if found, None otherwise.
    """
    game_modes = get_modes()
    try:
        for k, v in game_modes.items():
            if int(v) == int(mode):
                return k
        return None
    except Exception as e:
        logging.error(f"An error occurred while getting the game mode: {e}")
        return None
    
def get_mode_int(mode):
    """
    Returns the game mode integer corresponding to the given mode.

    Args:
        mode (str): The mode string to retrieve the integer for.

    Returns:
        int or None: The game mode integer if found, None otherwise.
    """
    game_modes = get_modes()
    try:
        for k, v in game_modes.items():
            if k.lower() == mode.lower():
                return int(v)
        return None
    except Exception as e:
        logging.error(f"An error occurred while getting the game mode: {e}")
        return None
    
@check_score
def calculate_result(game_mode, players) -> tuple :
    """
    Calculate the result of a game based on the game mode and players' scores.

    Args:
        game_mode (str): The game mode.
        players (dict): A dictionary containing players' names as keys and their scores as values.

    Returns:
        tuple: A tuple containing the calculated result and the game mode string.

    Raises:
        Exception: If an error occurs while calculating the result.
    """
    result = None
    game_mode_str = get_mode_string(game_mode)
    mode_int = game_mode
    try:
        if game_mode_str is not None:
            game_mode_str = game_mode_str.lower()
            all_scores = [int(s) for s in players.values() if isinstance(int(s), int)]
            if len(set(all_scores)) == 1:
                result = all_scores[0]
                mode_int = get_mode_int("Unanimity")
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
        return result, mode_int
    except Exception as e:
        logging.error(f"An error occurred while calculating the result: {e}")
        return result, game_mode