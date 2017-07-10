import registry as reg
from graphs import showGraphs
from player import Player
from territory import Territory

class Game:
    def __init__(self):
        self.turn = 0
        self.players = []
        self.territories = []

        for i in range(0, reg.player_count):
            self.players.append(Player())

        self.terr_conns = [[False for x in range(reg.territory_count)] for y in range(reg.territory_count)]

        for i in range(0, reg.territory_count):
            self.territories.append(Territory(i))
            self.terr_conns[i][i] = True
            if i != 0:
                self.terr_conns[i][i - 1] = True
                self.terr_conns[i - 1][i] = True


game = Game()
showGraphs(game)
