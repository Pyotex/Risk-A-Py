import registry as reg
import random

def generateMatrix():
    adj_mat = [[False for x in range(0, reg.territory_count)] for y in range(0, reg.territory_count)]

    #Generating a diagonally symmetrical matrix
    for i in range(0, reg.territory_count):
        for j in range(0, i):
            adj_mat[i][j] = bool(random.randint(0, 1))
            adj_mat[j][i] = adj_mat[i][j]

    #TODO:Implement flood fill for getting all components of a graph

    return adj_mat
