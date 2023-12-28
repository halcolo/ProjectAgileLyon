import statistics
from package.player import Player
from tools.db_utils import (
    db_get_doc,
    db_create_doc,
    db_delete_doc,
    db_get_player_by_email,
)
from datetime import datetime
from flask import session


# @Singleton
class Task:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, task_id: str, mode: str = "", id: str = ""):

        self.id: str
        self.task_id = task_id
        self.mode = mode

        if id != "":
            self.get_task_from_db(id)

        self.players = list()
        self.tasks = list()
        self.colleciton = "task"
        self.stimations = dict()
        self.squad_id = None
        self.final_score = None
        self.manager = None
        self.creation_date = None
        self.status = None
        self.task_mode = None

    def create_task(self, session_check=True):
        task = dict()
        task["task_id"] = self.task_id
        task["status"] = True
        if session_check:
            task["players"] = {session["player_id"]: 0}
            task["squad_id"] = session["squad_id"]
            task["manager"] = session["player_id"]
        task["creation_date"] = datetime.now()
        task["game_mode"] = self.mode
        task["final_score"] = 0
        document_id = db_create_doc(self.colleciton, task)
        print("document_id:", document_id)
        self.id = document_id

    def delete_task(self):
        print("deleting task:", self.id)
        db_delete_doc(self.colleciton, self.id)
        self.id = None

    def add_player(self, name, email):
        player = db_get_player_by_email(email)
        if player:
            self.players.append(player)
        # self.players.append(Player(name, email))

    def get_players(self):
        return self.players

    def create_planning(self, planning_name, card_quantity, tasks, game_mode):
        self.planning_name = planning_name
        self.card_quantity = card_quantity
        self.tasks = tasks
        self.game_mode = game_mode
        self.mode = None
        self.players = list()
        self.tasks = list()

    def to_dict(self):
        data = {
            "id": self.get_id(),
            "task_id": self.task_id,
            "stimations": self.stimations,
            "squad_id": self.squad_id,
            "final_score": self.final_score,
            "manager": self.manager,
            "creation_date": self.creation_date,
            "status": self.status,
            "task_mode": self.task_mode,
        }

        return data

    def check_data_exist(self):
        if self.task_id is None or self.task_id == "":
            return False
        return True

    def get_id(self):
        return self.id

    @classmethod
    def get_task_from_db(self, id, session_check=True):
        task_dict = db_get_doc("task", id)
        if task_dict is None:
            return None
        self.name = task_dict["task_id"]
        if session_check:
            self.stimations = task_dict["players"]
            self.squad_id = task_dict["squad_id"]
            self.manager = task_dict["manager"]
        self.final_score = task_dict["final_score"]
        self.creation_date = task_dict["creation_date"]
        self.status = task_dict["status"]
        self.task_mode = task_dict["game_mode"]

    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict["task_id"], task_dict["mode"])
