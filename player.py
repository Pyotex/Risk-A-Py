import registry as reg
import random

class Player:
    def __init__(self, game, number, aggressive):
        self.territories = []
        self.soldiers = reg.init_troops
        self.number = number
        self.game = game

        self.aggressive = aggressive
        self.regroup_tactic = 0

    def __str__(self):
        return "Player number: " + str(self.number)

    def getTerritoriesForAttack(self):
        available = []

        for terr in self.territories:
            if terr.soldiers >= 2:
                index = terr.number
                for i in range(0, reg.territory_count):
                    if self.game.terr_conns[index][i] == True:
                        if self.game.territories[i] not in available and self.game.territories[i].owner != self:
                            available.append((self.game.territories[i], terr))

        return available

    def getNewSoldiers(self):
        new_soldiers = max(3, len(self.territories) // 3)
        self.soldiers = self.soldiers + new_soldiers
        print("Got new soldiers: " + str(new_soldiers) + ", territories: " + str(len(self.territories)))

    def startPhase(self):
        print(self.__str__() + " Still in start phase")

        free = self.game.getFreeTerritories()
        territory = free[random.randint(0, len(free) - 1)]
        territory.obtainTerritory(self)

        print(self.__str__() + " Chose terr number: " + str(territory.number))

    def attackTerritories(self, strong=False):
        attackable = self.getTerritoriesForAttack()
        chosen = None
        from_terr = None
        for terr in attackable:
            if not chosen:
                chosen = terr[0]
                from_terr = terr[1]
                continue

            if strong:
                if terr[0].soldiers > chosen.soldiers:
                    chosen = terr[0]
                    from_terr = terr[1]
            else:
                if terr[0].soldiers < chosen.soldiers:
                    chosen = terr[0]
                    from_terr = terr[1]

        if chosen and from_terr:
            self.game.attackTerritory(from_terr, chosen)


    def attack(self):
        if self.aggressive:
            self.attackTerritories(strong=True)
        else:
            self.attackTerritories(strong=False)

    def randomSoldierGrouping(self):
        #TODO:Implement random soldier grouping
        pass

    def improveGoodTerritories(self):
        #TODO:Implement good territories improvement
        pass

    def improveBadTerritories(self):
        #TODO:Implement bad territories improvement
        pass

    def improveBorderTerritories(self):
        #TODO:Implement border territories improvement
        pass


    def regroupSoldiers(self):
        if self.regroup_tactic == 0:
            self.randomSoldierGrouping()
        elif self.regroup_tactic == 1:
            self.improveGoodTerritories()
        elif self.regroup_tactic == 2:
            self.improveBadTerritories()
        elif self.regroup_tactic == 3:
            self.improveBorderTerritories()

    def play(self):
        if len(self.territories) == reg.territory_count:
            self.game.game_over = True
            return


        if self.game.start_phase:
            self.startPhase()

        else:
            self.regroupSoldiers()
            if random.random() > 0.5:
                self.attack()

            else:
                self.getNewSoldiers()
                self.regroupSoldiers()