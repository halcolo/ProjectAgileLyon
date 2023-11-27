from flask import jsonify
from flask import request
from flask.views import MethodView
from packages.planning_poker import PlanningPoker
from utils.utils import response


class PlayerView(MethodView):
    # Example usage:
    def __init__(self) -> None:
        super().__init__()
        
    def get(self):
        
        return jsonify({"message": "Hello, world!"})
    
    def post(self):
        name = request.args.get('name')
        self.game.add_player(name)
        return response("Player added")