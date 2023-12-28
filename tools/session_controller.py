from flask import session
import logging


def set_sessions(**kwargs):
    try:
        for key, value in kwargs.items():
            session[key] = value
    except KeyError:
        logging.error(f"Session variable {key} not setted correctly")
        return None


def get_sessions(*args):
    try:
        data = dict()
        for arg in args:
            data[arg] = session[arg]
        return data
    except KeyError:
        logging.error(f"Session variable {arg} not found")
        return None


def clear_sessions():
    session.clear()
    logging.info("Sessions cleared")
