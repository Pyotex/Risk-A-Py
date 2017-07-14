from territory import Territory
from graphs import showGraphs
from player import Player
import registry as reg
import random
import utils
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

        self.terr_conns = utils.generateMatrix()

        for i in range(0, reg.territory_count):
            self.territories.append(Territory(i))
            self.terr_conns[i][i] = True

    #Gets all territories without the owner
    def getFreeTerritories(self):
        free = []
        for terr in self.territories:
            if terr.owner is None:
                free.append(terr)
        if not free:
            self.start_phase = False

        return free

    #Gets all border territories
    def getBorderTerritories(self, territory):
        #TODO:Implement this function
        pass

    def rollDice(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second

    def attackTerritory(self, attacker, from_territory, attack_territory):
        first, second = self.rollDice()

        if first >= second:
            territory_won = attack_territory.attackTerritory(attacker, from_territory)
            return True, territory_won

        return False, None

game = Game()
showGraphs(game)

start = time.time()
running = False

#TODO:Break after winning or after n number of moves
while running:
    if game.game_over:
        running = False
        break

    if not game.getFreeTerritories():
        game.start_phase = False

    game.players[game.turn].play()
    game.turn = (game.turn + 1) % reg.player_count
