from flask import jsonify
from flask import request
from flask.views import MethodView
from utils.utils import response
from firebase_admin import auth


class PlayerView(MethodView):
    """
    A class representing the API endpoints for managing players.
    """

    def __init__(self) -> None:
        super().__init__()
        
    def get(self):
        """
        Get method for retrieving player information.

        Returns:
            A JSON response with a message.
        """
        return jsonify({"message": "Hello, world!"})
    

    def post(self):
        """
        Post method for adding a new player.

        Returns:
            A response indicating that the player has been added.
        """
        name = request.args.get('name')
        email = request.args.get('email')

        try:
            # user = auth.get_user_by_email(email)
            # If the user exists, retrieve the player
            player = self.game.get_player_by_email(email)
            if player:
                return response("Player already exists")
            else:
                self.game.add_player(name, email)
                return response("Player added")
        except auth.AuthError as e:
            # Handle the case when the user does not exist
            return response("User does not exist")

