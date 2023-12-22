from package.task import Task
from tools.db_utils import db_add_player_2_task
from tools.general_utils import update_task_points
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
        data = request.args.to_dict()
        self.put(task_id=data["TaskId"], 
                 game_name=data["TaskName"], 
                 score=data["btnradio"])
        return redirect("/")

    def post(self):
        """
        Handles POST requests for the game view.

        Returns:
            A redirect to the /game route.
        """
        data = request.form.to_dict()
        if "taskCode" in data.keys():
            db_add_player_2_task(
                player_id=session["player_id"], 
                task_id=data["taskCode"],
                )
            return redirect("/")
        planning_name = data["taskName"]
        game_mode = data["gameMode"]
        self.game = Task(planning_name, game_mode)
        self.game.create_task()
        return redirect("/")
    
    def put(self, task_id:str, game_name:str, score:str):
        """
        Handles PUT requests for the game view.

        Returns:
            A redirect to the /game route.
        """
        player_id = session["player_id"]
        update_task_points(player_id=player_id,
                           score=score, 
                           task_id=task_id)

