from utility import registry as reg


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

    def attack(self):
        self.player.getNewSoldiers()
