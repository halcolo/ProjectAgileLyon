from flask import jsonify
from flask import request
from flask.views import MethodView
from utils.utils import response


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
        self.game.add_player(name)
        # Player(name).create_user()
        return response("Player added")