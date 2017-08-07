class Territory:
    def __init__(self, number):
        self.owner = None
        self.soldiers = 0
        self.number = number

    def __repr__(self):
        return "Territory number: " + str(self.number)

    def obtainTerritory(self, new_owner):
        if self.owner:
            self.owner.territories.remove(self)
            self.owner = new_owner
            new_owner.territories.append(self)
            # self.soldiers = 1

        else:
            self.owner = new_owner
            self.soldiers = self.soldiers + 1
            new_owner.soldiers = new_owner.soldiers - 1
            new_owner.territories.append(self)
