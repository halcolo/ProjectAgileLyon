import statistics

class Player:
    def __init__(self, name):
        self.name = name
        self.estimate = None

    def enter_estimate(self, estimate):
        self.estimate = estimate

class PlanningPoker:
    def __init__(self):
        self.players = []
        self.modes = {
            "1":"Unanimity",
            "2":"Average",
            "3":"Median", 
            "4":"Majority",
            "5":"All"
            }
        self.mode = None
        
    # def select_game(self):
        
    def select_modes(self):
        mode_choice = True 
        while mode_choice:
            print("Game modes:")
            for i in self.modes:
                print(f"{i}: {self.modes[i]}")
                
            mode = str(input("Select a game mode: "))
            if mode in self.modes:
                self.mode = self.modes[mode]
                mode_choice = False

    def add_player(self, name):
        self.players.append(Player(name))

    def enter_estimates(self):
        for player in self.players:
            estimate = input(f"{player.name}, enter your estimate: ")
            player.enter_estimate(int(estimate))

    def reveal_estimates(self):
        for player in self.players:
            print(f"{player.name}'s estimate: {player.estimate}")

    def calculate_result(self):
        if self.mode == None:
            self.select_modes()
        estimates = [player.estimate for player in self.players]
        if self.mode == "Unanimity":
            if len(set(estimates)) == 1:
                print(f"Unanimity result: {estimates[0]}")
            else:
                print("No unanimity")
        elif self.mode == "Average":
            print(f"Average result: {sum(estimates) / len(estimates)}")
        elif self.mode == "Median":
            print(f"Median result: {statistics.median(estimates)}")
        elif self.mode == "Majority":
            print(f"Majority result: {max(set(estimates), key=estimates.count)}")
        elif self.mode == "All":
            if len(set(estimates)) == 1:
                print(f"Unanimity result: {estimates[0]}")
            else:
                print("No unanimity")
            print(f"Average result: {sum(estimates) / len(estimates)}")
            print(f"Median result: {statistics.median(estimates)}")
            print(f"Majority result: {max(set(estimates), key=estimates.count)}")
        

# Example usage:
game = PlanningPoker()
players = int(input("How many players? "))
for i in range(players):
    name = input(f"Player {i+1} name: ")
    game.add_player(name)
# game.add_player("Alice")
# game.add_player("Bob")
game.select_modes()
game.enter_estimates()
game.reveal_estimates()
game.calculate_result()
