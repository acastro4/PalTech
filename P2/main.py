from calendar import c
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import path
import robot
import plotlib
import cluster

SEED = 314
X = 2000
Y = 500
SIZE = 100
VEL = 1.38889 #M/S
T_EXT = 60 #S
C1 = "blue"
C2 = "purple"
C3 = "green"
C4 = "orange"
TYPEOFCLUSTER = 2 # 0: Vertical, 1: Horizontal, 2: 45º, 3: 25 puntos por robot angulo dinamico, 4: cluster KNN?
POS_ROBOT_1 = (X//2, 0, 0) # (pos x, pos y, index siempre 0)
POS_ROBOT_2 = (X//2, 0, 0) # (pos x, pos y, index siempre 0)
POS_ROBOT_3 = (X//2, 0, 0) # (pos x, pos y, index siempre 0)
POS_ROBOT_4 = (X//2, 0, 0) # (pos x, pos y, index siempre 0)

 # Seed
np.random.seed(SEED)

fig, ax = plt.subplots()

g1, g2, g3, g4 = cluster.getCluster(X, Y, SIZE, POS_ROBOT_1, POS_ROBOT_2, POS_ROBOT_3, POS_ROBOT_4, TYPEOFCLUSTER)

#print(len(g1), g1)
#print(len(g2), g2)
#print(len(g3), g3)
#print(len(g4), g4)

# Grafos por cluster
GF_1, pathFinal_1, recorrido_1, pathSimple1 = path.getTSPPath(g1, C1, ax, True)
GF_2, pathFinal_2, recorrido_2, pathSimple2 = path.getTSPPath(g2, C2, ax, True)
GF_3, pathFinal_3, recorrido_3, pathSimple3 = path.getTSPPath(g3, C3, ax, True)
GF_4, pathFinal_4, recorrido_4, pathSimple4 = path.getTSPPath(g4, C4, ax, True)

# Tiempos por cluster
tt1, tp1, te1 = robot.tiempoTotal(recorrido_1, VEL, T_EXT)
tt2, tp2, te2 = robot.tiempoTotal(recorrido_2, VEL, T_EXT)
tt3, tp3, te3 = robot.tiempoTotal(recorrido_3, VEL, T_EXT)
tt4, tp4, te4 = robot.tiempoTotal(recorrido_4, VEL, T_EXT)

# Imprimir Informacion de 
plotlib.printAll(VEL, T_EXT, [1, 2, 3, 4], [tt1, tt2, tt3, tt4], [tp1, tp2, tp3, tp4], [te1, te2, te3, te4], [pathSimple1, pathSimple2, pathSimple3, pathSimple4])


# graficar
plotlib.addToGraph(X, Y, SIZE, g1, g2, g3, g4, C1, C2, C3, C4, TYPEOFCLUSTER, POS_ROBOT_1)

limits=plt.axis('on') # turns on axis
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

seg_type = "vertical" if TYPEOFCLUSTER == 0 else "horizontal" if TYPEOFCLUSTER == 1 else "diagonal"
fig.suptitle(f'Mapa del recorrido usando segmentacion {seg_type} usando algoritmo TSP', fontsize=12)
plt.show()

