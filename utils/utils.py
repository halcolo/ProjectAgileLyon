from flask import jsonify
import secrets

def generate_token():
    return secrets.token_hex(16)

def response(message:str, status_code:int=200):
    resp = {
        "code": status_code,
        "message": message
        }
    return jsonify(resp), status_code
