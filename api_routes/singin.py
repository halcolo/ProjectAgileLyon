from package.player import Player
from tools.session_controller import set_sessions
from tools.db_utils import get_all_docs

# from config import db
from flask import render_template, redirect, request
from flask.views import MethodView


class Signin(MethodView):
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
        return render_template("signin.html", squads=get_all_docs("squad"))

    def post(self):
        # try:
        name, email, squad = (
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("squad"),
        )

        player = Player(name, email)
        try:
            player.get_player()
            print("getting player",name,squad)
            return render_template("login.html", error="Player already exists")
        except Exception as e:
            player.create_player(squad_id=squad)
        # Setting up session variables
        player_name, player_id = player.get_data()
        set_sessions(
            id=player_id,
            name=player_name,
            player_id=player.get_id(),
            squad_id=squad,
        )
        return redirect("/")
