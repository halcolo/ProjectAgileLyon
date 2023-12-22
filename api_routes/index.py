from package.player import Player, User
from config import db
from flask import render_template, session, redirect, request
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

        If the user is not logged in, redirect to the login page.
        Retrieve the enterprise ID and player ID from the session.
        Retrieve the modes dictionary from the database.
        Retrieve the list of games for the enterprise.
        Iterate through the games and retrieve the users for each game.
        Create a list of user objects with their scores.
        Create a list of task data for each game.
        Retrieve the cards dictionary from the database.
        Render the index.html template with the tasks list, modes, and cards.

        Returns:
            The rendered index.html template with the tasks list, modes, and cards.
        """
        if not session.get("name"):
            return redirect("login")

        enterprise_id = session["enterprise"]
        player_id = session["player_id"]

        modes = db.collection("dicts").document("modes").get().to_dict()

        games = db.collection("task").where("enterprise", "==", enterprise_id).get()
        tasks_list = list()
        for game in games:
            if player_id in game.to_dict().get("players"):
                users = list()
                for user_id, score in game.to_dict().get("players").items():
                    user_db = db.collection("users").document(user_id).get().to_dict()
                    user = User(user_db["name"])
                    user.set_id(user_id)
                    user_dict = user.to_dict()
                    user_dict["score"] = score
                    users.append(user_dict)
                data = {
                    'id': game.id,
                    'task_id': game.to_dict().get("task_id"),
                    'users': users,
                    'final_score': game.to_dict().get("final_score"),
                }
                tasks_list.append(data)
        
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
