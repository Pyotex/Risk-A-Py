import registry as reg
from game import Game
import time
from graphs import showGraphs

start = time.time()

for i in range(0, reg.max_repetition):
    game = Game()
    showGraphs(game)
    result, game_over = game.gameLoop()
    print(str(result) + " " + str(game_over))
    print(str(time.time() - start))