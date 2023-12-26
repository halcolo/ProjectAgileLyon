import logging
from config import db
from tools.db_utils import db_get_player_by_email

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
    def __init__(self, name, email):
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
            doc_ref = db.collection("player").document()
            self.set_id(doc_ref.id)
            doc_ref.set(
                {
                    "name": self.name,
                    "email": self.email,
                    "squad_id": "xzC8ollQoBJRv9l7ZhUG",
                }
            )
            self.squad_id = "xzC8ollQoBJRv9l7ZhUG"
            logging.info(f"User {self.name} created with id {self.get_id()}")

    def get_player_by_email(self, email):
        player = db_get_player_by_email(email)
        if player and len(player) > 0:
            return player
        
        return None
        # # Check if the player exists in Firebase
        # players_ref = db.collection("player")
        # query = players_ref.where("email", "==", email).limit(1)
        # results = query.get()
        # logging.info(f"Searching for player with email {email}")

        # for player_doc in results:
        #     player_data = player_doc.to_dict()
        #     player_data["id"] = player_doc.id
        #     logging.info(f"Player {player_data['name']} found : {player_data['email']}")
        #     return player_data

        # return None

    def get_squad(self):
        """
        Returns the squad associated with the player.

        Returns:
            str: The name of the squad.
        """
        return self.squad_id

