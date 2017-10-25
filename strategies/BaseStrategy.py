from utility import registry as reg
import operator
import random


class BaseStrategy:
    def __init__(self, player):
        self.player = player
        self.game = player.game

    # Returns a tuple (attackable_terr, attacking_from_terr)
    def getTerritoriesForAttack(self):
        available = []

        for terr in self.player.territories:
            # Make sure the territory we're attacking from has more than one soldier
            if terr.soldiers > 1:
                index = terr.number
                for i in range(0, reg.territory_count):
                    if self.game.terr_conns[index][i]:
                        if self.game.territories[i] not in available and self.game.territories[i].owner != self.player:
                            available.append((self.game.territories[i], terr))

        return available

    # Gets all border territories a.k.a. all the terrs that have a connection to an enemy terr
    def getBorderTerritories(self):
        border_terrs = []

        for terr in self.player.territories:
            for i in range(0, reg.territory_count):
                if self.game.terr_conns[terr.number][i] and self.game.territories[i].owner != self.player:
                    border_terrs.append(terr)
                    break

        return border_terrs

    def improveTerritories(self, good):
        #Sanity check
        if len(self.player.territories) == 0:
            return

        # Cuz i don't want to have two functions so i have to use this
        compare_sign = operator.gt if good else operator.lt

        average = self.player.averageSoldierCount()

        # Short for 'above_below_average' because I'm using this for improving good and bad terrs
        ab_average = []

        for terr in self.player.territories:
            if  compare_sign(terr.soldiers, average):
                ab_average.append(terr)

        if not ab_average:
            return

        rest_of_terrs = list(set(self.player.territories) - set(ab_average))

        for terr in rest_of_terrs:
            #Gets all connected terrs
            all_connected = self.game.getConnectedTerritories(self.game.terr_conns, terr)

            if not all_connected:
                return

            #List of good/bad connected terrs
            gb_connected = list(set(all_connected).intersection(set(ab_average)))

            if not gb_connected:
                return

            move_to = gb_connected[random.randint(0, len(gb_connected) - 1)]
            soldiers_to_move = random.randint(0, terr.soldiers - 1)

            move_to.soldiers += soldiers_to_move
            terr.soldiers -= soldiers_to_move

    def improveBorderTerritories(self):
        border_terrs = self.getBorderTerritories()

        rest_of_terrs = list(set(self.player.territories) - set(border_terrs))

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


    def attack(self):
        self.player.getNewSoldiers()
