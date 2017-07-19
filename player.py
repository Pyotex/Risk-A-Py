import registry as reg
import random
from graphs import showGraphs

class Player:
    def __init__(self, game, number, aggressive):
        self.territories = []
        self.soldiers = reg.init_troops
        self.number = number
        self.game = game
        self.dead = False

        if self.number < 4:
            self.aggressive = True
            self.regroup_tactic = self.number
        else:
            self.aggressive = False
            self.regroup_tactic = self.number - 4

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
        new_soldiers = int(pow(max(3, len(self.territories) // 3), 2))
        self.soldiers += new_soldiers
        #print("Got new soldiers: " + str(new_soldiers) + ", territories: " + str(len(self.territories)))

    def startPhase(self):
        #TODO:Improve territory choosing
        #print(self.__str__() + " Still in start phase")

        free = self.game.getFreeTerritories()
        territory = free[random.randint(0, len(free) - 1)]
        territory.obtainTerritory(self)

        #print(self.__str__() + " Chose terr number: " + str(territory.number))

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
        for terr in self.territories:
            soldiers_to_move = random.randint(0, self.soldiers)
            terr.soldiers += soldiers_to_move
            self.soldiers -= soldiers_to_move

        for terr in self.territories:
            connected = self.game.getConnectedTerritories(self.game.terr_conns, terr)

            if not connected:
                return

            move_to = connected[random.randint(0, len(connected) - 1)]
            soldiers_to_move = random.randint(0, terr.soldiers - 1)

            move_to.soldiers += soldiers_to_move
            terr.soldiers -= soldiers_to_move

    def calculateAverage(self):
        average = 0
        for terr in self.territories:
            average += terr.soldiers

        average = average / len(self.territories)

        return average

    def improveGoodTerritories(self):
        #Sanity check
        if len(self.territories) == 0:
            return

        average = self.calculateAverage()

        above_average = []

        for terr in self.territories:
            if terr.soldiers > average:
                above_average.append(terr)

        if not above_average:
            return

        rest_of_terrs = list(set(self.territories) - set(above_average))

        for terr in rest_of_terrs:
            #Gets all connected terrs
            all_connected = self.game.getConnectedTerritories(self.game.terr_conns, terr)

            if not all_connected:
                return

            #List of good connected terrs
            good_connected = list(set(all_connected).intersection(set(above_average)))

            if not good_connected:
                return

            move_to = good_connected[random.randint(0, len(good_connected) - 1)]
            soldiers_to_move = random.randint(0, terr.soldiers - 1)

            move_to.soldiers += soldiers_to_move
            terr.soldiers -= soldiers_to_move

    def improveBadTerritories(self):
        #Sanity check
        if len(self.territories) == 0:
            return

        average = self.calculateAverage()

        below_average = []

        for terr in self.territories:
            if terr.soldiers < average:
                below_average.append(terr)

        if not below_average:
            return

        rest_of_terrs = list(set(self.territories) - set(below_average))

        for terr in rest_of_terrs:
            #Gets all connected terrs
            all_connected = self.game.getConnectedTerritories(self.game.terr_conns, terr)

            if not all_connected:
                return

            #List of good connected terrs
            bad_connected = list(set(all_connected).intersection(set(below_average)))

            if not bad_connected:
                return

            move_to = bad_connected[random.randint(0, len(bad_connected) - 1)]
            soldiers_to_move = random.randint(0, terr.soldiers - 1)

            move_to.soldiers += soldiers_to_move
            terr.soldiers -= soldiers_to_move

    def getBorderTerritories(self):
        border_terrs = []

        for terr in self.territories:
            for i in range(0, reg.territory_count):
                if self.game.terr_conns[terr.number][i] and self.game.territories[i].owner != self:
                    border_terrs.append(terr)
                    break

        return border_terrs

    def improveBorderTerritories(self):
        border_terrs = self.getBorderTerritories()

        rest_of_terrs = list(set(self.territories) - set(border_terrs))

        for terr in rest_of_terrs:
            # Gets all connected terrs
            all_connected = self.game.getConnectedTerritories(self.game.terr_conns, terr)

            if not all_connected:
                return

            # List of good connected terrs
            border_connected = list(set(all_connected).intersection(set(rest_of_terrs)))

            if not border_connected:
                return

            move_to = border_connected[random.randint(0, len(border_connected) - 1)]
            soldiers_to_move = random.randint(0, terr.soldiers - 1)

            move_to.soldiers += soldiers_to_move
            terr.soldiers -= soldiers_to_move


    def regroupSoldiers(self):
        #TODO:Jesus Christ just optimize every piece of this dog shit...
        if self.regroup_tactic == 0:
            self.randomSoldierGrouping()
        elif self.regroup_tactic == 1:
            self.improveGoodTerritories()
        elif self.regroup_tactic == 2:
            self.improveBadTerritories()
        elif self.regroup_tactic == 3:
            self.improveBorderTerritories()

    def play(self):
        if self.dead:
            return

        if len(self.territories) == 0 and not self.game.start_phase:
            self.dead = True
            print("")
            print(self.__str__() + " donezo" + ", move: " + str(self.game.moves))
            for player in self.game.players:
                print(player.__str__() + " has: " + str(len(player.territories)) + " territories")

            showGraphs(self.game)
            return

        if len(self.territories) == reg.territory_count:
            self.game.game_over = True
            return


        if self.game.start_phase:
            self.startPhase()

        else:

            self.getNewSoldiers()
            self.regroupSoldiers()


            if random.random() > 0.5:
                self.attack()