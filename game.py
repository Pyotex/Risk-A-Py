from utility import utils, registry as reg
from utility.graphs import showGraphs
from territory import Territory
from player import Player
import random


class Game:
    def __init__(self):
        self.game_over = False
        self.start_phase = True

        self.turn = 0
        self.moves = 0

        self.players = [Player(self, i) for i in range(0, reg.player_count)]
        self.territories = [Territory(i) for i in range(0, reg.territory_count)]

        self.terr_conns = utils.generateMatrix()

    # Gets all territories without the owner
    def getFreeTerritories(self):
        free = []
        for terr in self.territories:
            if terr.owner is None:
                free.append(terr)
        if not free:
            self.start_phase = False

        return free

    # Gets all territories connected to the provided territory
    def getConnectedTerritories(self, matrix, terr):
        stack = [terr.number]

        connected = []

        while stack:
            pos = stack.pop()

            if self.territories[pos] not in connected and self.territories[pos].owner == terr.owner:
                # Cause we don't want the provided terr to be in the list
                if pos != terr.number:
                    connected.append(self.territories[pos])

                    for i in range(reg.territory_count):
                        if matrix[pos][i]:
                            stack.append(i)

        return connected

    # Fair dice roll
    @staticmethod
    def rollDice(attacker_terr, defender_terr):
        # Number of soldiers on both territories
        attack_soldiers = attacker_terr.soldiers
        defend_soldiers = defender_terr.soldiers

        # Rolling the required number of dices
        attack_dices = [random.randint(1, 6) for i in range(min(3, attack_soldiers - 1))]
        defend_dices = [random.randint(1, 6) for i in range(min(2, defend_soldiers - 1))]

        # Sorting dices in descending order
        attack_dices.sort(reverse=True)
        defend_dices.sort(reverse=True)

        for i in range(min(len(attack_dices), len(defend_dices))):
            if attack_dices[i] > defend_dices[i]:
                return True
            elif defend_dices[i] > attack_dices[i]:
                return False

        return False
        # TODO:Maybe, just maybe, fix this shit?
        # self.rollDice(attacker_terr, defender_terr)

    # Rolls the dice and if successful the attacker gets the territory
    def attackTerritory(self, attacker_terr, defender_terr):
        won = self.rollDice(attacker_terr, defender_terr)

        if won:
            defender_terr.obtainTerritory(attacker_terr.owner)
        else:
            attacker_terr.obtainTerritory(defender_terr.owner)

    # Gets the winner or the player(s) with the most territories
    def getBestPlayers(self):
        players = []
        max_terr_count = -1
        for player in self.players:
            if len(player.territories) > max_terr_count:
                if players:
                    players[0] = player
                else:
                    players.append(player)

            if len(player.territories) == max_terr_count:
                players.append(player)

            max_terr_count = len(player.territories)

        return players

    # Main game loop
    def gameLoop(self):

        while True:
            # TODO: Make it prettier
            if self.start_phase:
                self.getFreeTerritories()

            if not self.start_phase:
                showGraphs(self)

                if self.moves >= reg.max_moves or self.game_over:
                    return self.getBestPlayers(), self.game_over, self.moves

                self.moves += 1

            self.players[self.turn].play()
            self.turn = (self.turn + 1) % reg.player_count
