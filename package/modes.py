import statistics

class Estimation:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def stimations(self, player_id: str, stimation: int):
        self.stimations[player_id] = stimation
        
    def __average(self, estimations:list):
        return statistics.mean(estimations)
    
    def __median(self, estimations:list):
        return statistics.median(estimations)
    
    def __majority(self, estimations:list):
        return statistics.mode(estimations)
    
    def estimate(self, estimations:list):
        if self.name == "Average":
            return self.__average(estimations)
        elif self.name == "Median":
            return self.__median(estimations)
        elif self.name == "Majority":
            return self.__majority(estimations)

    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['id'], task_dict['name'])
