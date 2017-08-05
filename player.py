from strategies.StrategyRandom import StrategyRandom
from utility import registry as reg

class Player:
    def __init__(self, game, number, aggressive):
        self.territories = []
        self.soldiers = reg.init_troops
        self.number = number
        self.game = game
        self.dead = False

        self.strategy = StrategyRandom(self)

    def __repr__(self):
        return "Player number: " + str(self.number)

    def getTerritoriesForAttack(self):
        pass

    def getBorderTerritories(self):
        pass

    # Gets new soldiers based on territory count
    def getNewSoldiers(self):
        self.soldiers += max(3, len(self.territories))
        print("Has " + str(len(self.territories)) + " territories, got " + str(max(3, len(self.territories))) + " new soldiers")

    def play(self):
        if not self.game.start_phase:
            self.getNewSoldiers()

        self.strategy.play()