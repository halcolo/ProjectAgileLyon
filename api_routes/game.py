from flask import (render_template, 
                   redirect)
from flask.views import MethodView

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
        return redirect("/game")
