import statistics
from package.modes import Estimation
from package.player import Player
from tools.db_utils import db_get_doc, db_create_doc
from tools.class_utils import Singleton
from datetime import datetime
from flask import session


@Singleton
class Task:
    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self, task_id: str, mode:str='', id:str=''):
        
        self.id:str
        self.task_id = task_id
        self.mode = mode
        self.mode = None
        
        if self.id != '' and id is not None:
            self.get_task_from_db(id) 
            
        self.players = list()
        self.tasks = list()
        self.colleciton = "task"
        self.stimations = dict()
        self.enterprise = None
        self.final_score = None
        self.manager = None
        self.creation_date = None
        self.status = None
        self.task_mode = None
        self.estimation_type:Estimation
        

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
            'id': self.id,
            'name': self.name,
            'stimations': self.stimations,
            'enterprise': self.enterprise,
            'final_score': self.final_score,
            'manager': self.manager,
            'creation_date': self.creation_date,
            'status': self.status,
            'task_mode': self.task_mode,
        }
        
        return data

        
    @classmethod
    def check_data_exist(cls):
        if cls.task_id is None or cls.task_id == '':
            return False
        return True
    
    @classmethod
    def get_task_from_db(self, id):
        task_dict = db_get_doc('task', id)
        if task_dict is None:
            return None
        self.name = task_dict['task_id']
        self.stimations = task_dict['players']
        self.enterprise = task_dict['enterprise']
        self.final_score = task_dict['final_score']
        self.manager = task_dict['manager']
        self.creation_date = task_dict['creation_date']
        self.status = task_dict['status']
        self.task_mode = task_dict['game_mode']
           
    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['id'], task_dict['name'], task_dict['description'])