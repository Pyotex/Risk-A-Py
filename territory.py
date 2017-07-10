class Territory:
    def __init__(self, number):
        self.owner = None
        self.soldiers = 0
        self.number = number

    def __str__(self):
        return "Territory number: " + str(self.number)