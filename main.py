
#Programacion numerica y no numerica-tarea 6

    #ANDERSON ESCOBAR - DCN0501IIV1
    #ALBERT RANGEL - DCN0501IIV1

import numpy as np
import matplotlib.pyplot as plt
import libf

def f(x):
    return x**3 + x

def obtener_datos_usuario():
 

    while True:
        try:
            xi = float(input("Ingrese el valor inicial de x: "))
            xf = float(input("Ingrese el valor final de x: "))
            n = int(input("Ingrese el número de puntos: "))
            if n <= 0:
                print("El número de puntos debe ser mayor que cero.")
            else:
                return xi, xf, n
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números.")


def main():
    """Función principal del programa."""

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            xi, xf, n = obtener_datos_usuario()
            libf.plotf(f, xi, xf, n)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

def mostrar_menu():
    print("Calculadora de Funciones")
    print("------------------------")
    print("1: Graficar f(x) = x^3 + 3 = 2x")
    print("2: Salir")

if __name__ == "__main__":
    main()