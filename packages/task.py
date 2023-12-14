class Task:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.stimations = dict()

    def stimations(self, player_id: str, stimation: int):
        self.stimations[player_id] = stimation
