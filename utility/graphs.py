import matplotlib.pyplot as plt
import networkx as nx

from utility import registry as reg


def showAdjMatrix(game):
    plt.matshow(game.terr_conns)

def showGraph(game):
    G = nx.Graph()
    G.add_nodes_from(game.territories)

    soldiers = [str(terr.soldiers) for terr in game.territories]
    terr_numbers = [str(terr.number) for terr in game.territories]
    terr_owners = {}

    for i in range(len(game.territories)):
        if game.territories[i].owner is not None:
            terr_owners[i] = str(game.territories[i].owner.number)
        else:
            terr_owners[i] = "-1"

    labels = {}

    for i in range(0, reg.territory_count):
        labels[game.territories[i]] = terr_numbers[i] + ":" + terr_owners[i]

    for i in range(0, len(game.territories)):
        for j in range(0, len(game.territories)):
            if game.terr_conns[i][j] == True:
                G.add_edge(game.territories[i], game.territories[j])

    nx.draw_networkx(G, labels=labels)

def showGraphs(game):
    if reg.show_graph:
        showGraph(game)

    if reg.show_matrix:
        showAdjMatrix(game)

    plt.show()
