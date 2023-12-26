from package.player import Player, User
from tools.session_controller import get_sessions, set_sessions, clear_sessions
from tools.db_utils import db_get_doc, db_set_doc, db_get_doc_by_field
# from config import db
from flask import render_template, redirect, request
from flask.views import MethodView


class Index(MethodView):
    """Return Hello world message.

    This class represents the index view of the API. It inherits from the MethodView class.

    Methods:
        get: Handles the GET request for the index view.

    Attributes:
        None
    """

    def get(self):
        """
        Handle GET requests to the index route.

        If the player is not logged in, redirect to the login page.
        Retrieve the squad ID and player ID from the session.
        Retrieve the modes dictionary from the database.
        Retrieve the list of games for the squad.
        Iterate through the games and retrieve the player for each game.
        Create a list of player objects with their scores.
        Create a list of task data for each game.
        Retrieve the cards dictionary from the database.
        Render the index.html template with the tasks list, modes, and cards.

        Returns:
            The rendered index.html template with the tasks list, modes, and cards.
        """
        session_name = get_sessions("name")
        if not session_name:
            return redirect("login")

        session_vars = get_sessions("squad_id", "player_id")
        squad_id = session_vars["squad_id"]
        player_id = session_vars["player_id"]

        modes = db_get_doc("dicts", "modes")
        cards = db_get_doc("dicts", "cards")
        if cards:
            cards = cards.get("fibbo_13")
        else:
            cards = list((1, 3, 5, 8, 13, 21, 34, 55, 89, 'coffee'))
        games = db_get_doc_by_field("task", "squad_id", squad_id)
        tasks_list = list()
        # Set all tasks with players
        if len(games) > 0:
            for game in games:
                if player_id in game.get("players"):
                    player_scores = list()
                    for player_id, score in game.get("players").items():
                        player_db = db_get_doc("player", player_id)
                        player = User(player_db["name"])
                        player.set_id(player_id)
                        player_dict = player.to_dict()
                        player_dict["score"] = score
                        player_scores.append(player_dict)
                    data = {
                        'id': game.get("id"),
                        'task_id': game.get("task_id"),
                        'player': player_scores,
                        'final_score': game.get("final_score"),
                    }
                    tasks_list.append(data)
        
        return render_template("index.html", tasks_list=tasks_list, modes=modes, cards=cards)


class Login(MethodView):
    """Return the Login Page.

    This class is a subclass of MethodView and is responsible for handling the login functionality.
    It provides two methods: get() and post().

    Methods:
        get(): Renders the login.html template.
        post(): Handles the login form submission, sets the session variables, and redirects to the home page.

    Attributes:
        None
    """

    def get(self):
        return render_template("login.html")

    def post(self):
        try:
            name, email = request.form.get("name"), request.form.get("email")
            player = Player(name, email)
            
            # Setting up session variables
            player_name, player_id = player.get_data()
            set_sessions(
                id=player_id,
                name=player_name, 
                player_id=player.get_id(),
                squad_id=player.get_squad(),
            )
            return redirect("/")
        except Exception as e:
            return render_template("login", error=e)


class Logout(MethodView):
    """A class representing the logout functionality.

    This class provides methods to handle GET and POST requests for logging out.

    Methods:
        get(): Renders the login page.
        post(): Logs out the player by clearing the session and redirecting to the home page.
    """

    def get(self):
        """Render the login page."""
        clear_sessions()
        return redirect("login")

    def post(self):
        """Log out the player.

        This method clears the session and redirects the player to the home page.
        """
        clear_sessions()
        return redirect("/")
