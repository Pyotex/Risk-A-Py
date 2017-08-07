from .BaseStrategy import BaseStrategy
from random import randint


class StrategyRandom(BaseStrategy):
    def __init__(self, player):
        super().__init__(player)

    # Randomly chooses territories
    def startPhase(self):
        # Gets free terrs and chooses randomly
        available = self.game.getFreeTerritories()
        chosen = available[randint(0, len(available) - 1)]

        # Obtains the chosen territory
        chosen.obtainTerritory(self.player)

    # Randomly attacks territories
    def attack(self):
        attackable = self.getTerritoriesForAttack()
        if not attackable:
            return

        chosen, from_terr = attackable[randint(0, len(attackable) - 1)]

        self.game.attackTerritory(from_terr, chosen)

    # Randomly regroups soldiers between territories
    def regroupSoldiers(self):
        # Randomly places soldiers that were given at the beginning of the turn
        for terr in self.player.territories:
            soldiers_to_move = randint(0, self.player.soldiers)
            terr.soldiers += soldiers_to_move
            self.player.soldiers -= soldiers_to_move

        # Moves a random number of soldiers from one terr to a random terr
        for terr in self.player.territories:
            connected = self.game.getConnectedTerritories(self.game.terr_conns, terr)

            if not connected:
                return

            move_to = connected[randint(0, len(connected) - 1)]
            soldiers_to_move = randint(0, terr.soldiers - 1)

            move_to.soldiers += soldiers_to_move
            terr.soldiers -= soldiers_to_move

    # Random, again...decides if it should attack or not
    def play(self):
        if self.player.game.start_phase:
            self.startPhase()
        else:
            self.regroupSoldiers()
            self.attack()
