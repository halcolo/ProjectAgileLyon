import statistics
from config import db

class Player:
    def __init__(self, name):
        self.name = name
        self.create_user()
        self.id = None

    # def enter_estimate(self, task_id:str, stimate:int):
    #     task = tasks[task_id]
    #     task.stimations[self.id] = stimate
        
    def create_user(self): 
        doc_ref = db.collection("users").document()
        self.id = doc_ref.id
        doc_ref.set({
            'name': self.name,
        })
        print(f"User {self.name} created with id {self.id}")
        
    def get_id(self):
        return self.id

class Task:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.stimations = dict()
        
    def stimations(self, player_id:str, stimation:int):
        self.stimations[player_id] = stimation
    
    
class PlanningPoker:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, id:str, mode:str):
        self.id = id
        self.players = list()
        self.mode = mode
        self.tasks = list()
        
    def create_task(self, task):
        self.tasks.append(task)
    
    def add_player(self, name):
        self.players.append(Player(name))

    def player_stimation_estimates(self):
        for player in self.players:
            estimate = input(f"{player.name}, enter your estimate: ")
            player.enter_estimate(int(estimate))

#     def reveal_estimates(self):
#         for player in self.players:
#             print(f"{player.name}'s estimate: {player.estimate}")

#     def calculate_result(self):
#         if self.mode == None:
#             self.select_modes()
#         estimates = [player.estimate for player in self.players]
#         if self.mode == "Unanimity":
#             if len(set(estimates)) == 1:
#                 print(f"Unanimity result: {estimates[0]}")
#             else:
#                 print("No unanimity")
#         elif self.mode == "Average":
#             print(f"Average result: {sum(estimates) / len(estimates)}")
#         elif self.mode == "Median":
#             print(f"Median result: {statistics.median(estimates)}")
#         elif self.mode == "Majority":
#             print(f"Majority result: {max(set(estimates), key=estimates.count)}")
#         elif self.mode == "All":
#             if len(set(estimates)) == 1:
#                 print(f"Unanimity result: {estimates[0]}")
#             else:
#                 print("No unanimity")
#             print(f"Average result: {sum(estimates) / len(estimates)}")
#             print(f"Median result: {statistics.median(estimates)}")
#             print(f"Majority result: {max(set(estimates), key=estimates.count)}")
        