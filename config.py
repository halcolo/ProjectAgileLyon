import os
from flask import Flask
from flask_session import Session
import firebase_admin
from firebase_admin import credentials, firestore

PORT = 3000
app = Flask(__name__, static_url_path="/static")

app.config["ENV"] = "production"
app.config["DEBUG"] = False
app.config["TESTING"] = False

app.config["SESSION_COOKIE_SECURE"] = (True,)  # Avoid session differents to HTTPS
app.config["SESSION_COOKIE_HTTPONLY"] = (True,)  # Avoid session lecture using JS
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax',
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_SECURE"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = 3600

Session(app)

# Configurar Firebase
path = os.path.dirname(os.path.abspath(__file__))
cred = credentials.Certificate(f"{path}/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
