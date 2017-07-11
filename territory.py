class Territory:
    def __init__(self, number):
        self.owner = None
        self.soldiers = 0
        self.number = number

    def __str__(self):
        return "Territory number: " + str(self.number)

    def obtainTerritory(self, new_owner):
        self.owner.territories.remove(self)
        self.owner = new_owner
        new_owner.territories.append(self)
