from random import randint
import registry as reg

class Player:
    def __init__(self, game, number):
        self.territories = []
        self.troops = reg.init_troops
        self.number = number
        self.game = game

    def __str__(self):
        return "Player number: " + str(self.number)

    def play(self):
        if self.game.start_phase:
            free = self.game.getFreeTerritories()
            if not free:
                self.game.game_over = True
                return
            territory = free[randint(0, len(free) - 1)]
            territory.owner = self
