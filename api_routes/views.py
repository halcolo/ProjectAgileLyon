from flask import (render_template, 
                   session, 
                   redirect, 
                   request)
from flask.views import MethodView
from utils.utils import generate_token

class Index(MethodView):
    """return Hello world message

    Args:
        MethodView (_type_): _description_
    """
    def get(self):
        if not session.get("name"):
            return redirect("/login")
        return render_template('index.html')
    

class Login(MethodView):
    """return Login Page

    Args:
        MethodView (_type_): _description_
    """
    def get(self):
        return render_template("login.html")
    
    def post(self):
        session["name"] = request.form.get("name")
        session["id"] = generate_token()
        return redirect("/")        
        
        
class Logout(MethodView):
    """return Login Page

    Args:
        MethodView (_type_): _description_
    """
    def get(self):
        return render_template("login.html")
    
    def post(self):
        session["name"] = request.form.get("name")
        session["id"] = generate_token()
        return redirect("/")   