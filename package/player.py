import logging
from config import db

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
        self.get_user()

    def get_user(self):
        """
        Get the user from the database.
        """
        player = self.get_player_by_email(self.email)
        if player:
            self.set_id(player["id"])
            self.name = player["name"]
            self.email = player["email"]
            self.enterprise = player["enterprise"]
            logging.info(f"Player {self.name} found with id {self.get_id()}")
        
    def create_user(self):
            """
            Creates a new user in the database with the provided name and email.
            """
            doc_ref = db.collection("users").document()
            self.set_id(doc_ref.id)
            doc_ref.set(
                {
                    "name": self.name,
                    "email": self.email,
                }
            )
            logging.info(f"User {self.name} created with id {self.get_id()}")

    def get_player_by_email(self, email):
        # Check if the player exists in Firebase
        players_ref = db.collection("users")
        query = players_ref.where("email", "==", email).limit(1)
        results = query.get()
        logging.info(f"Searching for player with email {email}")

        for player_doc in results:
            player_data = player_doc.to_dict()
            player_data["id"] = player_doc.id
            logging.info(f"Player {player_data['name']} found : {player_data['email']}")
            return player_data

        return None

    def get_enterprise(self):
        """
        Returns the enterprise associated with the player.

        Returns:
            str: The name of the enterprise.
        """
        return self.enterprise

