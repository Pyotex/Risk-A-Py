from utility import registry as reg
from game import Game
import time

start = time.time()

for i in range(0, reg.max_repetition):
    game = Game()
    players, game_over, moves = game.gameLoop()
    # TODO: Print the best player(s)