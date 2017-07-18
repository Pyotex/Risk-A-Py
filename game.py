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
            self.players.append(Player(self, i, bool(random.randint(0, 1))))

        self.terr_conns = utils.generateMatrix(self.territories)

        for i in range(0, reg.territory_count):
            self.territories.append(Territory(i))

    #Gets all territories without the owner
    def getFreeTerritories(self):
        free = []
        for terr in self.territories:
            if terr.owner is None:
                free.append(terr)
        if not free:
            self.start_phase = False

        return free

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


    def rollDice(self, attacker_terr, defender_terr):
        #Number of soldiers on both territories
        attack_soldiers = attacker_terr.soldiers
        defend_soldiers = defender_terr.soldiers

        #Rolling the required number of dices
        attack_dices = [ random.randint(1, 6) for i in range(min(3, attack_soldiers - 1))]
        defend_dices = [ random.randint(1, 6) for i in range(min(3, defend_soldiers - 1))]

        #Sorting dices in descending order
        attack_dices.sort(reverse=True)
        defend_dices.sort(reverse=True)

        for i in range(min(len(attack_dices), len(defend_dices))):
            if attack_dices[i] > defend_dices[i]:
                return True
            elif defend_dices[i] > attack_dices[i]:
                return False

        return False
        #self.rollDice(attacker_terr, defender_terr)

    def attackTerritory(self, attacker_terr, defender_terr):
        won = self.rollDice(attacker_terr, defender_terr)

        if won:
            defender_terr.obtainTerritory(attacker_terr.owner)
        else:
            attacker_terr.obtainTerritory(defender_terr.owner)


    def gameLoop(self):
        running = True

        while running:
            if not self.start_phase:
                self.moves = self.moves + 1

            if self.game_over or self.moves >= reg.max_moves:
                running = False
                max = 0
                best = -1
                for player in self.players:
                    if len(player.territories) > max:
                        max = len(player.territories)
                        best = player.number

                if not self.game_over:
                    for player in self.players:
                        print(player.__str__() + " has: " + str(len(player.territories)) + " territories")

                return best, self.game_over

            # This method already has a check if empty
            self.getFreeTerritories()

            self.players[self.turn].play()
            self.turn = (self.turn + 1) % reg.player_count
        return -1, False
