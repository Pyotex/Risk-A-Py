import matplotlib.pyplot as plt
import networkx as nx

def showGraphs(game):
    G = nx.Graph()
    G.add_nodes_from(game.territories)

    for i in range(0, len(game.territories)):
        for j in range(0, len(game.territories)):
            if game.terr_conns[i][j] == True:
                G.add_edge(game.territories[i], game.territories[j])

    nx.draw_networkx(G)
    plt.matshow(game.terr_conns)

    plt.show()
