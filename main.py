import os
import time
from buscaminas import crear_tablero, mostrar_tablero
from utils import pedir_entero

CONFIG_FILE = "config.txt"
TIEMPOS_FILE = "mejores_tiempos.txt"

# Leer configuración desde archivo
def leer_configuracion():
    filas, columnas, minas = 8, 8, 10
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            for line in f:
                if line.startswith('filas='):
                    filas = int(line.split('=')[1])
                elif line.startswith('columnas='):
                    columnas = int(line.split('=')[1])
                elif line.startswith('minas='):
                    minas = int(line.split('=')[1])
    return filas, columnas, minas

# Leer los mejores tiempos desde archivo
def leer_mejores_tiempos():
    tiempos = []
    if os.path.exists(TIEMPOS_FILE):
        with open(TIEMPOS_FILE, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    nombre, tiempo, filas, columnas = line.strip().split(',')
                    tiempos.append((nombre, float(tiempo), int(filas), int(columnas)))
    tiempos.sort(key=lambda x: x[1])
    return tiempos[:3]

# Guardar un nuevo tiempo si es de los mejores
def guardar_tiempo(nombre, tiempo, filas, columnas):
    tiempos = leer_mejores_tiempos()
    tiempos.append((nombre, tiempo, filas, columnas))
    tiempos.sort(key=lambda x: x[1])
    tiempos = tiempos[:3]
    with open(TIEMPOS_FILE, 'w') as f:
        f.write('# nombre,tiempo,filas,columnas\n')
        for n, t, fi, co in tiempos:
            f.write(f'{n},{t},{fi},{co}\n')

# Mostrar los mejores tiempos
def mostrar_mejores_tiempos():
    print("\n--- Mejores Tiempos ---")
    tiempos = leer_mejores_tiempos()
    if not tiempos:
        print("No hay récords aún.")
    else:
        for i, (nombre, tiempo, filas, columnas) in enumerate(tiempos, 1):
            print(f"{i}. {nombre} - {tiempo:.2f} segundos - Tablero: {filas}x{columnas}")
    print("----------------------\n")

# Menú de inicio
def menu_inicio():
    while True:
        print("1) Jugar\n2) Ver mejores tiempos\n3) Salir")
        op = pedir_entero("Seleccione una opción: ", 1, 3)
        if op == 2:
            mostrar_mejores_tiempos()
        elif op == 1:
            return True
        else:
            return False

# Función principal que controla el flujo del juego
def jugar():
    if not menu_inicio():
        return
    nombre = input("Ingrese su nombre: ")
    filas, columnas, minas = leer_configuracion()
    tablero = crear_tablero(filas, columnas, minas)
    descubiertas = [[False for _ in range(columnas)] for _ in range(filas)]
    inicio = time.time()
    while True:
        mostrar_tablero(tablero, descubiertas)
        print(f"Jugador: {nombre}")
        f = pedir_entero("Fila: ", 0, filas-1)
        c = pedir_entero("Columna: ", 0, columnas-1)
        if tablero[f][c] == 'M':
            print(f"¡BOOM! Has perdido, {nombre}.")
            mostrar_tablero(tablero, [[True]*columnas for _ in range(filas)])
            break
        descubiertas[f][c] = True
        if all((tablero[i][j] == 'M' or descubiertas[i][j]) for i in range(filas) for j in range(columnas)):
            fin = time.time()
            duracion = fin - inicio
            print(f"¡Felicidades {nombre}! Has ganado en {duracion:.2f} segundos.")
            mostrar_tablero(tablero, [[True]*columnas for _ in range(filas)])
            guardar_tiempo(nombre, duracion, filas, columnas)
            break

if __name__ == "__main__":
    jugar()