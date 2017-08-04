from utility import utils, registry as reg
from territory import Territory
from player import Player
import random

class Game:
    def __init__(self):
        self.turn = 0
        self.moves = 0
        self.players = [Player(self, i, bool(random.randint(0, 1))) for i in range(0, reg.player_count)]
        self.territories = [Territory(i) for i in range(0, reg.territory_count)]
        self.game_over = False
        self.start_phase = True
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
        stack = []
        stack.append(terr.number)

        connected = []

        while stack:
            pos = stack.pop()

            if self.territories[pos] not in connected and self.territories[pos].owner == terr.owner:
                #Cause we don't want the terr to be in the list
                if pos != terr.number:
                    connected.append(self.territories[pos])

                    for i in range(reg.territory_count):
                        if matrix[pos][i] == True:
                            stack.append(i)

        return connected

    # Fair dice roll
    def rollDice(self, attacker_terr, defender_terr):
        #Number of soldiers on both territories
        attack_soldiers = attacker_terr.soldiers
        defend_soldiers = defender_terr.soldiers

        #Rolling the required number of dices
        attack_dices = [ random.randint(1, 6) for i in range(min(3, attack_soldiers - 1))]
        defend_dices = [ random.randint(1, 6) for i in range(min(2, defend_soldiers - 1))]

        #Sorting dices in descending order
        attack_dices.sort(reverse=True)
        defend_dices.sort(reverse=True)

        for i in range(min(len(attack_dices), len(defend_dices))):
            print(attack_dices[i], defend_dices[i])
            if attack_dices[i] > defend_dices[i]:
                return True
            elif defend_dices[i] > attack_dices[i]:
                return False

        return False
        # TODO:Maybe, just maybe, fix this shit?
        #self.rollDice(attacker_terr, defender_terr)

    # Rolls the dice and if successful the attacker gets the territory
    def attackTerritory(self, attacker_terr, defender_terr):
        won = self.rollDice(attacker_terr, defender_terr)

        if won:
            defender_terr.obtainTerritory(attacker_terr.owner)
        else:
            attacker_terr.obtainTerritory(defender_terr.owner)

    # Gets the winner or the player(s) with the most territories
    def getBestPlayers(self):
        pass


    # Main game loop
    def gameLoop(self):
        running = True

        while running:
            # TODO: Make it prettier
            if self.start_phase:
                self.getFreeTerritories()

            if not self.start_phase:
                self.moves += 1

                if self.moves >= reg.max_moves or self.game_over:
                    running = False
                    return self.getBestPlayers(), self.game_over, self.moves

            self.players[self.turn].play()
            self.turn = (self.turn + 1) % reg.player_count
