import logging
from tools.db_utils import (
    db_get_player_by_email,
    db_delete_doc,
    db_create_doc,
)
import logging


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.__id: str

    def get_data(self) -> tuple:
        """
        Get the name and email of the player.

        Returns:
            tuple: A tuple containing the name and email of the player.
        """
        return self.name, self.__id

    def get_id(self):
        """
        Returns the ID of the player.

        Returns:
            int: The ID of the player.
        """
        return self.__id

    def set_id(self, id):
        """
        Sets the ID of the player.

        Args:
            id (int): The ID of the player.
        """
        self.__id = id

    def to_dict(self):
        """
        Returns a dictionary representation of the player.

        Returns:
            dict: A dictionary containing the name and email of the player.
        """
        return {
            "name": self.name,
            "id": self.get_id(),
        }


class Player(User):
    """
    Represents a player in the game.

    :param name: The name of the player.
    :type name: str
    :param email: The email address of the player.
    :type email: str
    """

    def __init__(self, name, email):
        """
        Initializes a new Player object.

        :param name: The name of the player.
        :type name: str
        :param email: The email address of the player.
        :type email: str
        """
        super().__init__(name)
        self.email = email
        self.squad_id: str
        self.get_player()

    def get_player(self):
        """
        Get the player from the database.
        """
        player = self.get_player_by_email(self.email)
        if player:
            self.set_id(player["id"])
            self.name = player["name"]
            self.email = player["email"]
            self.squad_id = player["squad_id"]
            logging.info(f"Player {self.name} found with id {self.get_id()}")
        else:
            self.create_player()

    def create_player(self):
        """
        Creates a new player in the database with the provided name and email.
        """
        squad_id = "xzC8ollQoBJRv9l7ZhUG"
        data = {
            "name": self.name,
            "email": self.email,
            "squad_id": squad_id,
        }
        result = db_create_doc("player", data)
        print(result)
        self.squad_id = squad_id
        self.set_id(result)
        logging.info(f"User {self.name} created with id {self.get_id()}")

    def delete_player(self):
        """
        Deletes the player from the database.
        """
        db_delete_doc("player", self.get_id())
        logging.info(f"Player {self.name} deleted with id {self.get_id()}")

    def get_player_by_email(self, email):
        """
        Retrieves a player from the database based on the provided email.

        :param email: The email of the player.
        :type email: str

        :return: The player data if found, None otherwise.
        :rtype: dict or None
        """
        player = db_get_player_by_email(email)
        if player and len(player) > 0:
            return player

        return None

    def get_squad(self):
        """
        Returns the squad associated with the player.

        :return: The name of the squad.
        :rtype: str
        """
        return self.squad_id
