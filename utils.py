# utils.py - Funciones auxiliares para Buscaminas
#
# Esta función pide al usuario un número entero dentro de un rango
# mensaje: el texto que se muestra al usuario
# minimo: valor mínimo aceptado
# maximo: valor máximo aceptado
# Devuelve el número ingresado por el usuario, validado

def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"El valor debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
