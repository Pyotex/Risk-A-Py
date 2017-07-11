from random import randint
import registry as reg

class Player:
    def __init__(self, game, number):
        self.territories = []
        self.troops = reg.init_troops
        self.number = number
        self.game = game

    def __str__(self):
        return "Player number: " + str(self.number)

    def getTerritoriesForAttack(self):
        available = []

        for terr in self.territories:
            index = terr.number
            for i in range(0, reg.territory_count):
                if self.game.terr_conns[index][i] == True and index != i:
                    if self.game.territories[i] not in available and self.game.territories[i].owner != self:
                        available.append(self.game.territories[i])

        return available

    def play(self):
        if self.game.start_phase:
            print(self.__str__() + " Still in start phase")
            free = self.game.getFreeTerritories()
            if not free:
                self.game.start_phase = False
                return
            territory = free[randint(0, len(free) - 1)]
            territory.owner = self
            self.territories.append(territory)
            print(self.__str__() + " Chose terr number: " + str(territory.number))
        else:
            print(self.__str__() + " Woo attacking")
            attack_terrs = self.getTerritoriesForAttack()
            territory = attack_terrs[randint(0, len(attack_terrs) - 1)]
            won = self.game.attackTerritory(self, territory)
            if won:
                print(self.__str__() + " Won terr number: " + str(territory.number))

            if len(self.territories) == reg.territory_count:
                self.game.game_over = True
                print(self.__str__() + " won yaaaaaaaaay")
