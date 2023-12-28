from package.player import Player, User
from tools.session_controller import get_sessions, set_sessions, clear_sessions
from tools.db_utils import db_get_doc, db_set_doc, db_get_doc_by_field
from tools.general_utils import get_mode_string

# from config import db
from flask import render_template, redirect, request
from flask.views import MethodView


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
        # try:
        name, email = request.form.get("name"), request.form.get("email")

        player = Player(name, email)
        try:
            player.get_player()
        except Exception as e:
            return render_template("login.html", error=e)

        # Setting up session variables
        player_name, player_id = player.get_data()
        set_sessions(
            id=player_id,
            name=player_name,
            player_id=player.get_id(),
            squad_id=player.get_squad(),
        )
        return redirect("/")

    # except Exception as e:
    #     print(e)
    #     return render_template("login.html", error=e)
