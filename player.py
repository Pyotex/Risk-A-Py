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

    def attack(self):
        # TODO:Implement attacking
        pass

    def defend(self):
        # TODO:Implement defending
        pass

    def play(self):
        #TODO:Decide if attacking or defending
        pass