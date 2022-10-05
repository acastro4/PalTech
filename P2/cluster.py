from calendar import c
import matplotlib.pyplot as plt
import numpy as np


def getRecta(p1, p2, ps, parametro):
    x1, y1 = p1
    x2, y2 = p2
    xs, ys = ps
    if x2 != x1:
        m = (y2 - y1) / (x2 - x1)
        # y - y1 = m * (x - x1) -> y = mx - mx1 + y1 -> y - mx < -mx1 + y1
        if parametro == ">=":
            return (ys - m * xs >= -m * x1 + y1)
        if parametro == ">":
            return (ys - m * xs > -m * x1 + y1)
        if parametro == "<=":
            return (ys - m * xs <= -m * x1 + y1)
        if parametro == "<":
            return (ys - m * xs < -m * x1 + y1)
    else:
        if parametro == ">=":
            return (xs >= x1)
        if parametro == ">":
            return (xs > x1)
        if parametro == "<=":
            return (xs <= x1)
        if parametro == "<":
            return (xs < x1)

    return np.NaN

def getCluster(x_s, y_s, size, pr1, pr2, pr3, pr4, typeofcluster): 
    # 0: 4 partes iguale dividias en 500x500

# Creación de puntos
    x = np.random.random_sample(size = size) * x_s
    y = np.random.random_sample(size = size) * y_s
    index_map = [x for x in range(1, (size + 1))]
    robot1 = pr1
    robot2 = pr2
    robot3 = pr3
    robot4 = pr4

    if typeofcluster == 0:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//4)]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//2) and a > (x_s//4)]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (3*x_s//4) and a > (x_s//2)]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s) and a > (3*x_s//4)]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4

    elif typeofcluster == 1:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (y_s//4)]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (y_s//2) and b > (y_s//4)]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (3*y_s//4) and b > (y_s//2)]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (y_s) and b > (3*y_s//4)]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4

    elif typeofcluster == 2:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((0, y_s), (pr1[0], pr1[1]), (a, b), "<")]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((0, y_s), (pr1[0], pr1[1]), (a, b), ">=") and getRecta((pr1[0], pr1[1]), (x_s//2, y_s), (a, b), "<")]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((pr1[0], pr1[1]), (x_s//2, y_s), (a, b), ">=") and getRecta((pr1[0], pr1[1]), (x_s, y_s), (a, b), ">=")]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((pr1[0], pr1[1]), (x_s, y_s), (a, b), "<")]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4

    else:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//4)]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//2) and a > (x_s//4)]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (3*x_s//4) and a > (x_s//2)]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s) and a > (3*x_s//4)]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4

if __name__ == "__main__":
    x1, y1 = 1000, 0
    x2, y2 = 0, 500
    xs, ys = 300, 100
    print(getRecta((x1, y1), (x2, y2), (xs, ys), "<="))
    plt.axline((x1, y1), (x2, y2), color='r')
    plt.scatter(xs, ys, c='b')
    plt.show()
