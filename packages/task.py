from packages.modes import Estimation

class Task:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.stimations = dict()
        self.estimation_type:Estimation

    def stimations(self, player_id: str, stimation: int):
        self.stimations[player_id] = stimation

    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['id'], task_dict['name'], task_dict['description'])
