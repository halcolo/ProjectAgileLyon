from flask import (Flask, 
                   render_template, 
                   redirect, request, 
                   session)
from flask.views import MethodView
from packages.planning_poker import PlanningPoker
from utils.utils import generate_token

class GameView(MethodView):
    # Example usage:
    def __init__(self) -> None:
        super().__init__()
        # self.game = PlanningPoker("1b32")
        
    def get(self):
        return render_template("game.html")
    
    def post(self):
        self.token = generate_token()
        print(self.token)
        # print(self.token)
        # session["token"] = self.token
        # session["game"] = PlanningPoker(self.token)
        # print(session["game"])
        # request_data = request.get_json()
        # return response(f"Game created {token}")
        return redirect("/game")   