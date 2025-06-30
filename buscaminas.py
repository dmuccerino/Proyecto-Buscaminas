import random

# Esta función crea el tablero de Buscaminas con minas y números
# filas: número de filas del tablero
# columnas: número de columnas del tablero
# minas: cantidad de minas a colocar
# Devuelve una matriz con 'M' para minas y números para casillas seguras

def crear_tablero(filas, columnas, minas):
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    minas_colocadas = 0
    # Colocamos minas aleatoriamente
    while minas_colocadas < minas:
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)
        if tablero[f][c] != 'M':
            tablero[f][c] = 'M'
            minas_colocadas += 1
    # Calculamos los números de casillas seguras (cantidad de minas alrededor)
    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c] == 'M':
                continue
            contador = 0
            for i in range(max(0, f-1), min(filas, f+2)):
                for j in range(max(0, c-1), min(columnas, c+2)):
                    if tablero[i][j] == 'M':
                        contador += 1
            tablero[f][c] = contador
    return tablero

# Esta función muestra el tablero en consola
# tablero: la matriz con minas y números
# descubiertas: matriz booleana que indica qué casillas están descubiertas
# marcadas: matriz booleana que indica dónde hay banderas

def mostrar_tablero(tablero, descubiertas, marcadas=None):
    filas = len(tablero)
    columnas = len(tablero[0])
    # Imprimimos los números de columna
    print("   " + " ".join([str(i) for i in range(columnas)]))
    for f in range(filas):
        fila = []
        for c in range(columnas):
            if marcadas and marcadas[f][c]:
                fila.append('🚩')  # Bandera
            elif descubiertas[f][c]:
                if tablero[f][c] == 'M':
                    fila.append('💣')  # Mostramos la mina
                else:
                    fila.append(str(tablero[f][c]))  # Mostramos el número
            else:
                fila.append('■')  # Casilla oculta
        print(f"{f:2} " + " ".join(fila))
