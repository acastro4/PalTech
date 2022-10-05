P2 Pregunta de diseño algorítmico:
==============================

Objetivo
-------------

1. Generar 100 puntos aleatorios (según una distribución uniforme) dentro de un rectángulo de lados 2000[m] y 500[m].
2. Divide los 100 puntos en 4 zonas según estimes conveniente y dentro de cada zona, planifica una ruta óptima al interior de cada una. Considera que todos los robots parten y terminan en un mismo punto (dado que deben ser transportados al campo con un camión).

Uso
---------------

1. Descargar codigo desde Github junto con las librerias de python: [Networkx](https://networkx.guide/), [Numpy](https://numpy.org/install/) y [Matplotlib](https://matplotlib.org/stable/users/installing/index.html) .
2. Ejecutar con python el archivo `main.py`.
3. Se mostrara el mapa de las plantas segmentadas y con el recorrido de cada robot, junto con la información del recorrido de cara robot.
4. Se pueden cambiar variables que permitiran ver y en un futuro optimizar los recorrido y segmentaciones.

Clustering
-------

Se implementaron 3 tipos clastering:
1. Separación del campo en lineas verticales (0).
2. Separación del campo en lineas horizontales (1).
3. Separación del campo en lineas diagonales (2).

Se opta por separar los puntos de esta forma ya que al distribuir de forma uniforme en todo el campo, si separamos el campo en iguales forma, cada segmento deberia tener una cantidad similar al resto de los demas.\

Variable: `TYPEOFCLUSTER`

Recorrido
-----------

Debido a la complejidad del problema, se utiliza la libreria `Networkx` para resolver el problema mediante el uso de grafos de la siguiente forma:

1. Se crea por segmento un grafo por segmento fully connected con pesos igual a su distancia entre los nodos.
2. Se resuelve mediante `Traveling Salesman Problem ` con el algoritmo `christofides`

Grafico
----------------

Se grafica en el mismo grafico los puntos, trajecto y segmentación.
