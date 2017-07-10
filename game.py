from territory import Territory
from graphs import showGraphs
from player import Player
import registry as reg
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

    def getFreeTerritories(self):
        free = []
        for terr in self.territories:
            if terr.owner is None:
                free.append(terr)
        return free


game = Game()
#showGraphs(game)

start = time.time()
running = True

while running:
    if time.time() - start > 2 or game.game_over:
        running = False
        break

    game.players[game.turn].play()
    game.turn = (game.turn + 1) % reg.player_count
