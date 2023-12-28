from package.player import Player, User
from config import db
from flask import render_template, session, redirect, request
from flask.views import MethodView


class Error(MethodView):
    def get(self, message):
        return render_template("error.html", error=message)
