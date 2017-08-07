import matplotlib.pyplot as plt
import networkx as nx

from utility import registry as reg


def showAdjMatrix(game):
    plt.matshow(game.terr_conns)


def showGraph(game):
    g = nx.Graph()
    g.add_nodes_from(game.territories)

    colors = [terr.owner.number for terr in game.territories]
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
        # 'n' stands for 'number', 'o' for 'owner' and 's' for 'soldiers'
        labels[game.territories[i]] = "n" + terr_numbers[i] + " o" + terr_owners[i] + " s" + soldiers[i]

    for i in range(0, len(game.territories)):
        for j in range(0, len(game.territories)):
            if game.terr_conns[i][j]:
                g.add_edge(game.territories[i], game.territories[j])

    if game.start_phase:
        nx.draw_networkx(g, labels=labels)
    else:
        nx.draw_networkx(g, node_color=colors, labels=labels)


def showGraphs(game):
    if reg.show_graph:
        showGraph(game)

    if reg.show_matrix:
        showAdjMatrix(game)

    plt.show()
