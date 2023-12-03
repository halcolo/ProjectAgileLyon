from flask import jsonify
import secrets

def response(message:str, status_code:int=200):
    """
    Creates a JSON response with the given message and status code.

    Args:
        message (str): The message to include in the response.
        status_code (int, optional): The HTTP status code. Defaults to 200.

    Returns:
        tuple: A tuple containing the JSON response and the status code.
    """
    resp = {
        "code": status_code,
        "message": message
    }
    return jsonify(resp), status_code
