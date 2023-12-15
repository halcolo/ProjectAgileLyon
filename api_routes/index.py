from config import db
from flask import render_template, session, redirect, request
from flask.views import MethodView
from packages.player import Player


class Index(MethodView):
    """Return Hello world message.

    This class represents the index view of the API. It inherits from the MethodView class.

    Methods:
        get: Handles the GET request for the index view.

    Attributes:
        None
    """

    def get(self):
        """Handles the GET request for the index view.

        If the session does not contain a "name" key, it redirects the user to the login page.
        Otherwise, it renders the index.html template.

        Args:
            None

        Returns:
            If the session does not contain a "name" key, it redirects the user to the login page.
            Otherwise, it renders the index.html template.
        """
        if not session.get("name"):
            return redirect("login")

        enterprise_id = session["enterprise"]
        player_id = session["player_id"]

        modes = db.collection("dicts").document("modes").get().to_dict()

        # modes = list(map(lambda x: x.to_dict().items(), modes))

        games = db.collection("task").where("enterprise", "==", enterprise_id).get()
        tasks_list = {
            game for game in games if player_id in game.to_dict().get("players")
        }
        cards = db.collection("dicts").document("cards").get().to_dict()['fibbo_13']
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
        name, email = request.form.get("name"), request.form.get("email")
        player = Player(name, email)
        session["name"], session["email"] = player.get_data()
        session["player_id"], session["enterprise"] = (
            player.get_id(),
            player.get_enterprise(),
        )
        return redirect("/")


class Logout(MethodView):
    """A class representing the logout functionality.

    This class provides methods to handle GET and POST requests for logging out.

    Methods:
        get(): Renders the login page.
        post(): Logs out the user by clearing the session and redirecting to the home page.
    """

    def get(self):
        """Render the login page."""
        session.clear()
        return redirect("login")

    def post(self):
        """Log out the user.

        This method clears the session and redirects the user to the home page.
        """
        session.clear()
        return redirect("/")
