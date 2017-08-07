from utility import registry as reg
from game import Game
import time

start = time.time()

for i in range(0, reg.max_repetition):
    game = Game()
    players, game_over, moves = game.gameLoop()

    if game_over:
        print(repr(players[0]) + " won after " + str(moves) + " moves!")

    else:
        for player in players:
            print(repr(player) + " has " + str(len(player.territories)) + " territories")
