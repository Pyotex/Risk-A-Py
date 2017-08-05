from .BaseStrategy import BaseStrategy
from random import randint

class StrategyRandom(BaseStrategy):

    def __init__(self, player):
        super().__init__(player)

    # Randomly chooses territories
    def startPhase(self):
        # Gets free terrs and chooses randomly
        available = self.game.getFreeTerritories()
        chosen = available[randint(0, len(available) - 1)]

        # Obtains the chosen territory
        chosen.obtainTerritory(self.player)
        print(repr(self.player) + " chose " + repr(chosen))

    # Randomly attacks territories
    def attack(self):
        print("attack")

    # Randomly regroups soldiers between territories
    def regroupSoldiers(self):
        print("regroup soldiers")

    # Random, again...decides if it should attack or not
    def play(self):
        if self.player.game.start_phase:
            self.startPhase()
        else:
            self.regroupSoldiers()
            self.attack()
