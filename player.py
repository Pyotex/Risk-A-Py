from random import randint
import registry as reg

class Player:
    def __init__(self, game, number):
        self.territories = []
        self.soldiers = reg.init_troops
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
                        available.append((self.game.territories[i], terr))

        return available

    def getNewSoldiers(self):
        new_soldiers = max(3, len(self.territories) // 3)
        self.soldiers = self.soldiers + new_soldiers
        print("Got new soldiers: " + str(new_soldiers) + ", territories: " + str(len(self.territories)))

    def fortifyPosition(self, won_territory):
        #TODO:Implement soldier regrouping
        pass

    def moveSoldiers(self):
        #TODO:move soldiers to the territory from which you wish to attack
        pass

    def startPhase(self):
        print(self.__str__() + " Still in start phase")

        free = self.game.getFreeTerritories()
        territory = free[randint(0, len(free) - 1)]
        territory.obtainTerritory(self)

        print(self.__str__() + " Chose terr number: " + str(territory.number))

    def play(self):
        if self.game.start_phase:
            self.startPhase()
        else:
            self.getNewSoldiers()

            attack_terrs = self.getTerritoriesForAttack()

            if not attack_terrs:
                return

            print(self.__str__() + " Woo attacking")

            attack_terr, original_terr = attack_terrs[randint(0, len(attack_terrs) - 1)]

            if original_terr.soldiers < 2:
                print("Not enough soldiers")
                self.moveSoldiers()
                return

            won, won_territory = self.game.attackTerritory(self, original_terr, attack_terr)

            if won:
                print(self.__str__() + " Won terr number: " + str(attack_terr.number))
                self.fortifyPosition(won_territory)

            if len(self.territories) == reg.territory_count:
                self.game.game_over = True
                print(self.__str__() + " won yaaaaaaaaay")
