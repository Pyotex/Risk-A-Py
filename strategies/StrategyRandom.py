from .BaseStrategy import BaseStrategy

class StrategyRandom(BaseStrategy):

    def __init__(self, player):
        super().__init__(player)

    # Randomly chooses territories
    def startPhase(self):
        pass

    # Randomly attacks territories
    def attack(self):
        pass

    # Randomly regroups soldiers between territories
    def regroupSoldiers(self):
        pass

    # Random, again...decides if it should attack or not
    def play(self):
        if self.player.game.start_phase:
            self.startPhase()
