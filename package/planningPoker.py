import statistics
from tools.class_utils import Singleton
from package.player import Player
from datetime import datetime
from flask import session
from tools.general_utils import db_create_doc


@Singleton
class Task:
    def __init__(self, task_id: str, mode: str):
        self.id: str
        self.task_id = task_id
        self.mode = mode
        self.players = list()
        self.tasks = list()
        self.colleciton = "task"

    def create_task(self):
        task = dict()
        task["task_id"] = self.task_id
        task["status"] = True
        task["players"] = {session["player_id"]: 0}
        task["enterprise"] = session["enterprise"]
        task["creation_date"] = datetime.now()
        task["game_mode"] = self.mode
        task["manager"] = session["player_id"]
        task["final_score"] = 0
        db_create_doc(self.colleciton, task)

    def add_player(self, name, email):
        self.players.append(Player(name, email))

    def player_stimation_estimates(self):
        for player in self.players:
            estimate = input(f"{player.name}, enter your estimate: ")
            player.enter_estimate(int(estimate))

    def create_planning(self, planning_name, card_quantity, tasks, game_mode):
        self.planning_name = planning_name
        self.card_quantity = card_quantity
        self.tasks = tasks
        self.game_mode = game_mode
        self.mode = None
        self.players = list()
        self.tasks = list()

