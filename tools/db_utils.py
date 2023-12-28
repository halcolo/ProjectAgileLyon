from config import db
from flask import jsonify


def response_message(message: str, status_code: int = 200):
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
            document = db.collection(collection_name).add(data)
            return document[1].id
        else:
            db.collection(collection_name).document(data["id"]).set(data)
        return response_message(
            f"Document created successfully in collection {collection_name}"
        )
    except Exception as e:
        return response_message(
            f"An error occurred while creating the document: {e}", 500
        )


def db_delete_doc(collection_name: str, doc_id: str):
    """
    Delete a document from the specified collection.

    Args:
        collection_name (str): The name of the collection to delete the document from.
        doc_id (str): The ID of the document to delete.

    Returns:
        str: A response message indicating the success or failure of the operation.
    """
    try:
        db.collection(collection_name).document(doc_id).delete()
        return response_message(
            f"Document deleted successfully from collection {collection_name}"
        )
    except Exception as e:
        print("error deleting document:", e)
        return response_message(
            f"An error occurred while deleting the document: {e}", 500
        )


def db_add_player_2_task(player_id: str, task_id: str):
    """
    Add a player to a task in the database.

    Args:
        player_id (str): The ID of the player to be added.
        task_id (str): The ID of the task to which the player will be added.

    Returns:
        str: A response message indicating the success or failure of the operation.
    """
    try:
        game = db_get_doc("task", task_id)
        players = game["players"]
        players[player_id] = 0
        game["players"] = players
        # print("setting up:", game)
        db.collection("task").document(task_id).set(game)
        return response_message(f"Player {player_id} added to game {task_id}")
    except Exception as e:
        return response_message(
            f"An error occurred while adding player {player_id} to game {task_id}: {e}",
            500,
        )


def db_get_doc(collection_name: str, doc_id: str) -> dict:
    """
    Retrieve a document from the specified collection.

    Args:
        collection_name (str): The name of the collection to retrieve the document from.
        doc_id (str): The ID of the document to retrieve.

    Returns:
        dict: A dictionary containing the document data.
    """
    try:
        doc = db.collection(collection_name).document(doc_id).get().to_dict()
        return doc
    except Exception as e:
        return response_message(
            f"An error occurred while retrieving the document: {e}", 500
        )


def db_get_doc_by_field(collection_name: str, field: str, value: str) -> list:
    """
    Retrieve a document from the specified collection.

    Args:
        collection_name (str): The name of the collection to retrieve the document from.
        field (str): The field to filter the document by.
        value (str): The value of the field to filter the document by.

    Returns:
        dict: A dictionary containing the document data.
    """
    docs = list()
    try:
        doc = db.collection(collection_name).where(field, "==", value).get()
        if len(doc) > 0:
            for d in doc:
                data = d.to_dict()
                data["id"] = d.id
                docs.append(data)

        return docs
    except Exception as e:
        return response_message(
            f"An error occurred while retrieving the document: {e}", 500
        )


def db_set_doc(collection_name: str, doc_id: str, data: dict) -> dict:
    """
    Update a document in the specified collection.

    Args:
        collection_name (str): The name of the collection to update the document in.
        doc_id (str): The ID of the document to update.
        data (dict): The data to be updated in the document.

    Returns:
        str: A response message indicating the success or failure of the operation.
    """
    try:
        db.collection(collection_name).document(doc_id).set(data)
        return response_message(
            f"Document updated successfully in collection {collection_name}"
        )
    except Exception as e:
        return response_message(
            f"An error occurred while updating the document: {e}", 500
        )


def db_get_player_by_email(player_email: str) -> dict:
    """
    Retrieve a player document from the database.

    Args:
        player_email (str): The email of the player to retrieve.

    Returns:
        dict: A dictionary containing the player data.
    """
    try:
        player_records = (
            db.collection("player").where("email", "==", player_email).get()
        )
        if len(player_records) > 0:
            player = player_records[0].to_dict()
            player["id"] = player_records[0].id
            return player
        else:
            return dict()

    except Exception as e:
        return response_message(
            f"An error occurred while retrieving the player: {e}", 500
        )
