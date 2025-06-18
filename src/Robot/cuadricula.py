import heapq
from queue import Full
import time
import os
import robot
import socket





# Movimientos (arriba, abajo, izquierda, derecha)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ultima_pos = (0, 0)

# Calcula el costo hasta el objetivo
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Hace un escaneo de los vecinos durante le ejecución del algoritmo
def obtener_vecinos(pos, filas, columnas):
    vecinos = []
    for dx, dy in movimientos:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            vecinos.append((nx, ny))
    return vecinos

# Muestra la matriz
def imprimir_matriz(matriz, pos_robot):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, fila in enumerate(matriz):
        linea = ""
        for j, val in enumerate(fila):
            if (i, j) == pos_robot:
                linea += "A "
            elif val == 0:
                linea += ". "
            elif val == 1:
                linea += "# "
            elif val == 2:
                linea += "2 "
        print(linea)
    time.sleep(0.2)

# Mueve el robot
"""
def mover_robot(matriz, pos_robot):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, fila in enumerate(matriz):
        linea = ""
        for j, val in enumerate(fila):
            if (i, j) == pos_robot:
                if pos_robot[0] < ultima_pos[0]:
                    robot.adelante()
                    time.sleep(5)
                    robot.detener()
                elif pos_robot[0] > ultima_pos[0]:
                    robot.atras()
                    time.sleep(5)
                    robot.detener()
                elif pos_robot[1] < ultima_pos[1]:
                    robot.izquierda()
                    time.sleep(1)
                    robot.adelante()
                    time.sleep(5)
                    robot.derecha()
                    time.sleep(1)
                    robot.detener()
                elif pos_robot[1] > ultima_pos[1]:
                    robot.derecha()
                    time.sleep(1)
                    robot.adelante()
                    time.sleep(5)
                    robot.izquierda()
                    time.sleep(1)
                    robot.detener()
                ultima_pos = pos_robot
                linea += "A "
            elif val == 0:
                linea += ". "
            elif val == 1:
                linea += "# "
            elif val == 2:
                linea += "2 "
        print(linea)
    time.sleep(0.2)
"""

# Algoritmo y lógica de recorrido
def a_estrella(matriz, inicio, objetivo):
    filas, columnas = len(matriz), len(matriz[0])
    pos_robot = inicio
    bandera = False

    # Información para la búsqueda
    while True:
        heap = []
        heapq.heappush(heap, (0, pos_robot))
        came_from = {}
        g_score = {pos_robot: 0}
        visitados = set()

        encontrado = False

        while heap:
            _, actual = heapq.heappop(heap)

            if actual in visitados:
                continue
            visitados.add(actual)

            if objetivo in obtener_vecinos(actual, filas, columnas):
                encontrado = True
                break

            for vecino in obtener_vecinos(actual, filas, columnas):
                if matriz[vecino[0]][vecino[1]] == 1:
                    continue

                tentative_g = g_score[actual] + 1
                if vecino not in g_score or tentative_g < g_score[vecino]:
                    g_score[vecino] = tentative_g
                    f = tentative_g + heuristica(vecino, objetivo)
                    heapq.heappush(heap, (f, vecino))
                    came_from[vecino] = actual

        if not encontrado:
            print("No se puede llegar al objetivo.")
            return

        # reconstruir el camino y moverse un paso
        actual = objetivo
        while actual not in came_from and not bandera:
            actual = min(obtener_vecinos(actual, filas, columnas), key=lambda n: g_score.get(n, float('inf')))
        camino = []
        while actual != pos_robot and not bandera:
            camino.append(actual)
            actual = came_from[actual]
            time.sleep(0.2)
        camino.reverse()

        if not camino:
            print("El robot ya está adyacente al objetivo.")
            return
        #simulacro de encontrar un obstaculo en el camino
        if len(camino) == 2:
            matriz[2][3] = 1 
            
        # Mover al siguiente paso
        pos_robot = camino[0]
        imprimir_matriz(matriz, pos_robot)

        

        # De cumplirse este if, significa que el robot llego a su objetivo
        if len(camino) == 1:
            bandera = True

        

        '''for vecino in obtener_vecinos(actual, filas, columnas):
            if matriz[vecino[0]][vecino[1]] == 2:
                print("El agente ya está adyacente al objetivo.")
                return'''

# Crear una matriz, Aqui es donde pueden meter los obstaculos que hayan
def crear_matriz_20x20():
    matriz = [[0 for _ in range(20)] for _ in range(20)]
    matriz[0][1] = 1
    return matriz

# Inicialización
# Valores de inicio y objetivo modificables
matriz = crear_matriz_20x20()
inicio = (0, 0)
ultima_pos = inicio
objetivo = (3, 3)
matriz[objetivo[0]][objetivo[1]] = 2

"""
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('nosequeipserialaqueusamos', 456))
mesa_que_ordeno = client_socket.recv(1024).decode()

# Ajustar con las posiciones que se van a usar
match mesa_que_ordeno:
    case '1':
        objetivo = (3, 3)
    case '2':
        objetivo = (3, 3)
    case '3':
        objetivo = (3, 3)
    case 'volver':
        objetivo = (0, 0)
"""    

# Ejecutar el algoritmo
a_estrella(matriz, inicio, objetivo)