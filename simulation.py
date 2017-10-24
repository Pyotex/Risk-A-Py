from utility import registry as reg, logging, graphs
from game import Game
import time

start = time.time()

wins = [0 for i in range(reg.player_count)]

for i in range(0, reg.max_repetition):
    game = Game()
    players, game_over, moves = game.gameLoop()

    if game_over:
        print(repr(players[0]) + " won after " + str(moves) + " moves!")
        logging.writeline(repr(players[0]) + " won after " + str(moves) + " moves!")

        wins[players[0].number] += 1

    else:
        for player in players:
            print(repr(player) + " has " + str(len(player.territories)) + " territories")

print(str(wins))
print('Finished after: ' + str(time.time() - start))
logging.writeline(str(wins))
logging.closeFile()
