import registry as reg
from game import Game
import time

start = time.time()

for i in range(0, reg.max_repetition):
    game = Game()
    result, game_over, moves = game.gameLoop()
    print(str(result) + ", " + str(game_over) + ", moves: " + str(moves))
    print(str(time.time() - start))