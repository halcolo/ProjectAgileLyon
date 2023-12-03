from flask import (render_template, 
                   session, 
                   redirect, 
                   request)
from flask.views import MethodView
from packages.planning_poker import Player

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
            return redirect("/login")
        return render_template('index.html')
    
    

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
        name = request.form.get("name")
        session["name"] = name
        Player(name)
        session['player_id'] = Player(name).id
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
        return render_template("login.html")
    
    def post(self):
        """Log out the user.

        This method clears the session and redirects the user to the home page.
        """
        session.clear()
        return redirect("/")
