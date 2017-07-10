import registry as reg

class Game:
    def __init__(self):
        self.turn = 0
        self.players = []

        for i in range(0, reg.player_count):
            self.players.append(Player())

        self.terr_conns = [[False for x in range(reg.territory_count)] for y in range(reg.territory_count)]

        for i in range(0, reg.territory_count):
            territory = Territory()
            self.terr_conns[i][i] = True



class Player:
    def __init__(self):
        self.territories = []
        self.troops = reg.init_troops



class Territory:
    def __init__(self):
        self.owner = None
        self.soldiers = 0

game = Game()