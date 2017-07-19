import matplotlib.pyplot as plt
import registry as reg
import networkx as nx

def showAdjMatrix(game):
    plt.matshow(game.terr_conns)

def showGraph(game):
    G = nx.Graph()
    G.add_nodes_from(game.territories)

    colors = [terr.owner.number for terr in game.territories]
    soldiers = [str(terr.soldiers) for terr in game.territories]

    labels = {}

    for i in range(0, reg.territory_count):
        labels[game.territories[i]] = soldiers[i]

    for i in range(0, len(game.territories)):
        for j in range(0, len(game.territories)):
            if game.terr_conns[i][j] == True:
                G.add_edge(game.territories[i], game.territories[j])

    nx.draw_networkx(G, node_color=colors, labels=labels)

def showGraphs(game):
    if reg.show_graph:
        showGraph(game)

    if reg.show_matrix:
        showAdjMatrix(game)

    plt.show()
