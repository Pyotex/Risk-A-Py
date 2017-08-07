from utility import registry as reg
import random


# Gets all components of a graph
# A graph component is a set of nodes which are all connected somehow
def getGraphComponent(matrix, start_terr):
    stack = [start_terr]

    connected = []

    while stack:
        pos = stack.pop()

        if pos not in connected:
            # You have to include the start_terr itself because you're finding components...
            connected.append(pos)

            for i in range(reg.territory_count):
                if matrix[pos][i]:
                    stack.append(i)

    return connected


def getAllGraphComponents(matrix):
    terrs = list(range(0, reg.territory_count))
    components = []

    while len(terrs) != 0:
        component = getGraphComponent(matrix, terrs[random.randint(0, len(terrs) - 1)])
        components.append(component)

        terrs = list(set(terrs) - set(component))

    return components


def connectComponents(components, adj_mat):
    if len(components) > 1:
        terr = components[0][random.randint(0, len(components[0]) - 1)]
        for i in range(1, len(components)):
            second_terr = components[i][random.randint(0, len(components[i]) - 1)]
            adj_mat[terr][second_terr] = True
            adj_mat[second_terr][terr] = True


def generateMatrix():
    adj_mat = [[False for x in range(0, reg.territory_count)] for y in range(0, reg.territory_count)]

    # Stands for terrs per player
    tpp = reg.terrs_per_player

    for i in range(0, reg.player_count):
        for j in range(i * tpp, i * tpp + tpp):
            for k in range(i * tpp, i * tpp + tpp):
                rnd_bool = False

                if random.random() < reg.connection_factor:
                    rnd_bool = True

                adj_mat[j][k] = rnd_bool
                adj_mat[k][j] = rnd_bool

    components = getAllGraphComponents(adj_mat)

    connectComponents(components, adj_mat)

    return adj_mat
