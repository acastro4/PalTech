import datetime
from calendar import c
import matplotlib.pyplot as plt
import numpy as np

VEL = 1.38889 #M/S
T_EXT = 60 #S

def printRoboInfo(vel, t_ext, index_robot, tt, tp, te, pathSimple):
    print()
    print(" Robot {} ".center(40, "#").format(index_robot))
    print()
    print(" CONSTANTES ".center(40, "-"))
    print()
    print("VELOCIDAD ROBOT: {} [M/S]".format(VEL))
    print("TIEMPO POR PLANTA: {} [S]".format(T_EXT))
    print()
    print(" Recorrido ".center(40, "-"))
    print()
    print("Planta Totales: {}".format((len(pathSimple) - 2)))
    print("Tiempo Total: {:0>8}".format(str(datetime.timedelta(seconds=int(tt)))))
    print("Tiempo de recorrido: {:0>8}".format(str(datetime.timedelta(seconds=int(tp)))))
    print("Tiempo de extracción: {:0>8}".format(str(datetime.timedelta(seconds=int(te)))))
    print()



def printAll(vel, t_ext, index_robots, tts, tps, tes, pathsSimples):
    for i in range(len(index_robots)):
        printRoboInfo(vel, t_ext, index_robots[i], tts[i], tps[i], tes[i], pathsSimples[i])

def addToGraph(x, y, size, g1, g2, g3, g4, c1, c2, c3, c4, typeofcluster, pos_robot):
    x1 = [a[0] for a in g1]
    y1 = [a[1] for a in g1]

    x2 = [a[0] for a in g2]
    y2 = [a[1] for a in g2]

    x3 = [a[0] for a in g3]
    y3 = [a[1] for a in g3]

    x4 = [a[0] for a in g4]
    y4 = [a[1] for a in g4]


    plt.scatter(x1, y1, c=c1,  alpha=0.5)
    plt.scatter(x2, y2, c=c2,  alpha=0.5)
    plt.scatter(x3, y3, c=c3,  alpha=0.5)
    plt.scatter(x4, y4, c=c4,  alpha=0.5)

    if typeofcluster == 0:
        plt.axvline(x//4, color='r') # vertical
        plt.axvline(x//2, color='r') # vertical
        plt.axvline(3*x//4, color='r') # vertical

    if typeofcluster == 1:
        plt.axhline(y//4, color='r') # vertical
        plt.axhline(y//2, color='r') # vertical
        plt.axhline(3*y//4, color='r') # vertical
    
    if typeofcluster == 2:
        sl1 = np.tan(np.radians(45))
        sl2 = np.tan(np.radians(90))
        sl3 = np.tan(np.radians(135))
        plt.axline((pos_robot[0], pos_robot[1]), (0, y), color='r')
        plt.axline((pos_robot[0], pos_robot[1]), (pos_robot[0], pos_robot[1] + y), color='r')
        plt.axline((pos_robot[0], pos_robot[1]), (x, y), color='r')


if __name__ == "__main__":
    tt = 4191.012215238746 
    tp = 2571.0122152387457 
    te = 1620
    n_ext = 23
    printAll(VEL, T_EXT, [1], [tt], [tp], [te], [n_ext])
