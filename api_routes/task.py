from packages.planningPoker import Task
from utils.utils import db_add_player_2_task
from flask import (
    render_template,
    redirect,
    request,
    session,
)
from flask.views import MethodView


class TaskView(MethodView):
    """
    View class for handling game related requests.
    """

    def __init__(self) -> None:
        super().__init__()
        self.game: Task

    def get(self):
        """
        Handles GET requests for the game view.

        Returns:
            The rendered game.html template.
        """
        return render_template("/")

    def post(self):
        """
        Handles POST requests for the game view.

        Returns:
            A redirect to the /game route.
        """
        data = request.form.to_dict()
        if data["gameCode"]:
            db_add_player_2_task(session["player_id"], data["gameCode"])
            return redirect("/")
        planning_name = data["taskName"]
        game_mode = data["gameMode"]
        self.game = Task(planning_name, game_mode)
        self.game.create_task()
        return redirect("/")
