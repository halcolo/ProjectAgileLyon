from flask import (render_template, redirect)
from flask.views import MethodView
from flask import request
from config import db


class GameView(MethodView):
    """
    View class for handling game related requests.
    """

    def __init__(self) -> None:
        super().__init__()
        
    def get(self):
        """
        Handles GET requests for the game view.
        
        Returns:
            The rendered game.html template.
        """
        return render_template("game.html")
    
    def post(self):
        """
        Handles POST requests for the game view.
        
        Returns:
            A redirect to the /game route.
        """
        planning_name = request.form.get("planningName")
        data = request.form.get("task1")
        print(planning_name)
        print(data)
        return redirect("/game")
