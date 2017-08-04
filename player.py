from strategies.StrategyRandom import StrategyRandom
from utility import registry as reg

class Player:
    def __init__(self, game, number, aggressive):
        self.territories = []
        self.soldiers = reg.init_troops
        self.strategy = StrategyRandom(self)
        self.number = number
        self.game = game
        self.dead = False

    def __repr__(self):
        return "Player number: " + str(self.number)

    def getTerritoriesForAttack(self):
        pass

    def getBorderTerritories(self):
        pass

    # Gets new soldiers based on territory count
    def getNewSoldiers(self):
        pass

    def play(self):
        self.strategy.play()