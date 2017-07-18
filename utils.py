import registry as reg
import random

def getGraphComponent(matrix, start_terr):
    #TODO:Fix bug with adding itself
    stack = []
    stack.append(start_terr)

    connected = []

    while stack:
        pos = stack.pop()

        if pos not in connected:
            #You have to include the start_terr itself because you're finding components...
            connected.append(pos)

            for i in range(reg.territory_count):
                if matrix[pos][i] == True:
                    stack.append(i)

    return connected

def getAllGraphComponents(matrix):
    terrs = list(range(0, reg.territory_count))
    components = []

    while len(terrs) != 0:
        component = getGraphComponent(matrix, terrs[random.randint(0, len(terrs) - 1)])
        components.append(component)

        terrs = list(set(terrs) - set(component))

    #print(len(components))
    return components


def generateMatrix(territories):
    adj_mat = [[False for x in range(0, reg.territory_count)] for y in range(0, reg.territory_count)]

    #Arguments for flood fill
    start_terr = 0

    #Generating a diagonally symmetrical matrix
    for i in range(0, reg.territory_count):
        for j in range(0, i):
            rnd_bool = False

            if random.random() < 0.06:
                rnd_bool = True
            adj_mat[i][j] = rnd_bool
            if rnd_bool == True:
                start_terr = i

            adj_mat[j][i] = adj_mat[i][j]

    terrs = list(range(0, reg.territory_count))

    components = getAllGraphComponents(adj_mat)

    if len(components) > 1:
        terr = components[0][random.randint(0, len(components[0]) - 1)]
        for i in range(1, len(components)):
            second_terr = components[i][random.randint(0, len(components[i]) - 1)]
            adj_mat[terr][second_terr] = True
            adj_mat[second_terr][terr] = True

    return adj_mat
