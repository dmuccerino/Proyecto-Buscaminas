import unittest
from buscaminas import crear_tablero

# Pruebas automáticas para la lógica de Buscaminas
class TestBuscaminas(unittest.TestCase):
    # Verifica que el tablero tenga el tamaño correcto
    def test_tamanio_tablero(self):
        filas, columnas, minas = 8, 8, 10
        tablero = crear_tablero(filas, columnas, minas)
        self.assertEqual(len(tablero), filas)
        self.assertEqual(len(tablero[0]), columnas)

    # Verifica que el número de minas sea el correcto
    def test_numero_de_minas(self):
        filas, columnas, minas = 8, 8, 10
        tablero = crear_tablero(filas, columnas, minas)
        total_minas = sum(row.count('M') for row in tablero)
        self.assertEqual(total_minas, minas)

if __name__ == "__main__":
    unittest.main()
