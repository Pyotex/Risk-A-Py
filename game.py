from territory import Territory
from graphs import showGraphs
from player import Player
import registry as reg
import random
import time

class Game:
    def __init__(self):
        self.turn = 0
        self.players = []
        self.territories = []
        self.game_over = False
        self.start_phase = True

        for i in range(0, reg.player_count):
            self.players.append(Player(self, i))

        self.terr_conns = [[False for x in range(reg.territory_count)] for y in range(reg.territory_count)]

        for i in range(0, reg.territory_count):
            self.territories.append(Territory(i))
            self.terr_conns[i][i] = True
            if i != 0:
                self.terr_conns[i][i - 1] = True
                self.terr_conns[i - 1][i] = True

    #Gets all territories without the owner
    def getFreeTerritories(self):
        free = []
        for terr in self.territories:
            if terr.owner is None:
                free.append(terr)
        if not free:
            self.start_phase = False

        return free

    # #Gets all territories with whom the provided territory borders with
    # def getBorderTerritories(self, territory):
    #     terrs = []
    #     index = territory.number
    #
    #     for i in range(0, reg.territory_count):
    #         if self.terr_conns[index][i] == True:
    #             terrs.append(self.territories[i])
    #
    #     return terrs

    def rollDice(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second

    def attackTerritory(self, attacker, from_territory, attack_territory):
        # if from_territory.soldiers < 2:
        #     print("Not enough soldiers")
        #     return False

        first, second = self.rollDice()

        if first >= second:
            attack_territory.attackTerritory(attacker, from_territory)
            return True

        return False

game = Game()
#showGraphs(game)

start = time.time()
running = True

while running:
    if game.game_over:
        running = False
        break

    if not game.getFreeTerritories():
        game.start_phase = False

    game.players[game.turn].play()
    game.turn = (game.turn + 1) % reg.player_count
