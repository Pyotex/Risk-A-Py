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
        self.moves = 0
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
        #TODO:Implement getter for border territories
        pass

    def rollDice(self):
        #TODO:Implement dice roll
        pass

game = Game()
showGraphs(game)

running = True

while running:
    if not game.start_phase:
        game.moves = game.moves + 1

    if game.game_over or game.moves >= reg.max_moves:
        running = False
        break

    #This method already has a check if empty
    game.getFreeTerritories()

    game.players[game.turn].play()
    game.turn = (game.turn + 1) % reg.player_count
