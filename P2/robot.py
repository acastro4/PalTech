import path
import numpy as np

VEL = 1.38889 #M/S
T_EXT = 60 #S

def tiempoTotal(pathList, vel_robot, tiempo_ext):
    
    t_path = sum([path_elem/vel_robot for path_elem in pathList])
    t_ext = tiempo_ext * (len(pathList) - 1)
    t_total = t_ext + t_path
    return t_total, t_path, t_ext
    


if __name__ == "__main__":
     # Seed
    np.random.seed(1)

    # Creación de puntos
    x = np.random.random_sample(size = 100) * 2000
    y = np.random.random_sample(size = 100) * 500
    index_map = [x for x in range(100)]
    robot1 = (1000, 0, 0)

    g1 = [ (a, b, i) for a, b, i in zip(x, y, index_map) if a <= 500]
    GF, pathFinal, pathList = path.getTSPPath(g1, True)
    tt, tp, te = tiempoTotal(pathList, VEL, T_EXT)
    print(tt, tp, te)






