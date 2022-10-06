from calendar import c
from operator import le
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

def getRectaS(p1, p2, ps, parametro):
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
    return False

def get25Elem(x, y, index_map, x_s, y_s, size, pr1):
    i, j = 0, 0 # bordes
    bordes = []
    direccion = 0 # 0: arriba, 1: derecha, 2: abajo
    while True:
        g1 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRecta((i, j), (pr1[0], pr1[1]), (a, b), "<")]
        if len(g1) >= size//4:
            bordes.append((i, j))
            break
        if direccion == 0:
            if j < y_s:
                j += 1
            else:
                direccion = 1
                i += 1

        elif direccion == 1:
            if i <= x_s:
                i += 1
            else:
                direccion = 2
                j -= 1    
    print(bordes, direccion) 
    while True:
        if i < x_s // 2:
            g2 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRectaS((bordes[-1][0], bordes[-1][1]), (pr1[0], pr1[1]), (a, b), ">=") and getRectaS((pr1[0], pr1[1]), (i, j), (a, b), "<") and (a, b, m) not in g1]
        else:
           g2 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRectaS((bordes[-1][0], bordes[-1][1]), (pr1[0], pr1[1]), (a, b), ">=") and getRectaS((pr1[0], pr1[1]), (i, j), (a, b), ">") and (a, b, m) not in g1]
        
        if len(g2) >= size//4:
            bordes.append((i, j))
            break
        if direccion == 0:
            if j < y_s:
                j += 1
            else:
                direccion = 1
                i += 1

        elif direccion == 1:
            if i <= x_s:
                i += 1
            else:
                direccion = 2
                j -= 1 
        else:
            j -= 1
    print(bordes, direccion) 
    print(i, j)
    while True:
        if bordes[-1][0] < x_s//2:
            if i < x_s//2:
                g3 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRectaS((pr1[0], pr1[1]), (bordes[-1][0], bordes[-1][1]), (a, b), ">=") and getRectaS((pr1[0], pr1[1]), (i, j), (a, b), "<=") and (a, b, m) not in g1  and (a, b, m) not in g2]
            else:
                g3 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRectaS((pr1[0], pr1[1]), (bordes[-1][0], bordes[-1][1]), (a, b), ">=") and getRectaS((pr1[0], pr1[1]), (i, j), (a, b), ">=") and (a, b, m) not in g1  and (a, b, m) not in g2]
        elif bordes[-1][0] > x_s//2:
            g3 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRectaS((pr1[0], pr1[1]), (bordes[-1][0], bordes[-1][1]), (a, b), "<=") and getRectaS((pr1[0], pr1[1]), (i, j), (a, b), ">=") and (a, b, m) not in g1  and (a, b, m) not in g2]
                   
        if len(g3) >= size//4:
            bordes.append((i, j))
            break
        if direccion == 0:
            if j < y_s:
                j += 1
            else:
                direccion = 1
                i += 1

        elif direccion == 1:
            if i <= x_s:
                i += 1
            else:
                direccion = 2
                j -= 1   
    print(bordes, direccion) 
    while True:
        g4 = [ (a, b, m) for a, b, m in zip(x, y, index_map) if getRectaS((pr1[0], pr1[1]), (i, j), (a, b), "<")]
        if len(g4) >= size//4:
            bordes.append((i, j))
            break
        if direccion == 0:
            if j < y_s:
                j += 1
            else:
                direccion = 1
                i += 1

        elif direccion == 1:
            if i <= x_s:
                i += 1
            else:
                direccion = 2
                j -= 1 
  
    return g1, g2, g3, g4, bordes
        #g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((0, y_s), (pr1[0], pr1[1]), (a, b), ">=") and getRecta((pr1[0], pr1[1]), (x_s//2, y_s), (a, b), "<")]
        
        #g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((pr1[0], pr1[1]), (x_s//2, y_s), (a, b), ">=") and getRecta((pr1[0], pr1[1]), (x_s, y_s), (a, b), ">=")]
        
        #g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((pr1[0], pr1[1]), (x_s, y_s), (a, b), "<")]



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
    bordeSegmento = []
    
        

    if typeofcluster == 0:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//4)]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//2) and a > (x_s//4)]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (3*x_s//4) and a > (x_s//2)]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s) and a > (3*x_s//4)]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4, bordeSegmento

    elif typeofcluster == 1:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (y_s//4)]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (y_s//2) and b > (y_s//4)]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (3*y_s//4) and b > (y_s//2)]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if b <= (y_s) and b > (3*y_s//4)]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4, bordeSegmento

    elif typeofcluster == 2:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((0, y_s), (pr1[0], pr1[1]), (a, b), "<")]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((0, y_s), (pr1[0], pr1[1]), (a, b), ">=") and getRecta((pr1[0], pr1[1]), (x_s//2, y_s), (a, b), "<")]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((pr1[0], pr1[1]), (x_s//2, y_s), (a, b), ">=") and getRecta((pr1[0], pr1[1]), (x_s, y_s), (a, b), ">=")]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if getRecta((pr1[0], pr1[1]), (x_s, y_s), (a, b), "<")]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4, bordeSegmento

    elif typeofcluster == 3:
        g1, g2, g3, g4, bordeSegmento =  get25Elem(x, y, index_map, x_s, y_s ,size, pr1)
        g1.insert(0, robot1)
        g2.insert(0, robot2)
        g3.insert(0, robot3)
        g4.insert(0, robot4) 
        return g1, g2, g3, g4, bordeSegmento
        
    else:
        g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//4)]
        g1.insert(0, robot1)
        g2 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s//2) and a > (x_s//4)]
        g2.insert(0, robot2)
        g3 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (3*x_s//4) and a > (x_s//2)]
        g3.insert(0, robot3)
        g4 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= (x_s) and a > (3*x_s//4)]
        g4.insert(0, robot4) 
        return g1, g2, g3, g4, bordeSegmento

if __name__ == "__main__":
    np.random.seed(314)
    size = 100
    x = np.random.random_sample(size = size) * 2000
    y = np.random.random_sample(size = size) * 500
    index_map = [x for x in range(1, (size + 1))]
    robot1 = (1000, 0, 0)
    get25Elem(x, y, index_map, 2000, 500, size, robot1)
