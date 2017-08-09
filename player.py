from strategies.StrategyRandom import StrategyRandom
from utility import registry as reg


class Player:
    def __init__(self, game, number):
        self.territories = []
        self.soldiers = reg.init_troops
        self.number = number
        self.game = game
        self.dead = False

        # Has to be after the self.game is set because the strategy requires the game instance
        self.strategy = StrategyRandom(self)

    def __repr__(self):
        return "Player number: " + str(self.number)

    # Gets new soldiers based on territory count
    def getNewSoldiers(self):
        self.soldiers += max(3, len(self.territories))

    def play(self):
        if len(self.territories) == 0 and not self.game.start_phase:
            return

        if not self.game.start_phase:
            self.getNewSoldiers()

        self.strategy.play()

        if len(self.territories) == reg.territory_count:
            self.game.game_over = True
