from calendar import c
from glob import glob1
from operator import le
from zipfile import Path
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def getDis(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    return np.sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2))


def getTSPPath(g1, typeofTSP, color, ax, bool_vis=False):
    G1 = nx.Graph()
    G2 = nx.Graph()

    for p in g1:
        G1.add_node(p[2])
        G2.add_node(p[2])

    for p1 in g1:
        for p2 in g1:
            if p1 == p2:
                continue
            G1.add_weighted_edges_from([(p1[2], p2[2], getDis(p1, p2))])


    tsp = nx.approximation.traveling_salesman_problem
    if typeofTSP == 0:
        path_tsp = tsp(G1, cycle=True, method= nx.approximation.christofides)
    else:
        path_tsp = tsp(G1, cycle=True, method=nx.approximation.greedy_tsp)
        
    path_list = [(path_tsp[i],  path_tsp[i+1]) for i in range(len(path_tsp)-1)]

    G2.add_edges_from(path_list)

    path_w_list = [G1.get_edge_data(edge[0], edge[1])["weight"] for edge in path_list]
    
    

    if not bool_vis: return G2, path_list, path_w_list, path_tsp

    pos = {i: (x, y) for (x, y, i) in g1}
    
    # Dibuja una imagen de red
    #nx.draw(G1,pos,with_labels=True, node_color='white', edge_color='b', node_size=800, alpha=0.5)
    nx.draw(G2,pos,with_labels=True, node_color=color, edge_color=color, node_size=400, alpha=0.5, ax=ax)

    #plt.show()
    return G2, path_list, path_w_list, path_tsp


if __name__ == "__main__":
     # Seed
    np.random.seed(1)

    # Creación de puntos
    x = np.random.random_sample(size = 100) * 2000
    y = np.random.random_sample(size = 100) * 500
    index_map = [x for x in range(100)]
    robot1 = (1000, 0, 0)

    #g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= 500]
    g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= 1000 and a > 500]
    g2.insert(0, robot1)
    GF, pathFinal, recorrido = getTSPPath(g2, "blue", True)
    print(pathFinal, recorrido)



