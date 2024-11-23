import os
import numpy as np
import matplotlib.pyplot as plt
import libf

def f(x):
    """Función a graficar."""
    return x**3 + x

def obtener_datos_usuario():
    """Solicita y obtiene los datos del usuario."""
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

def mostrar_menu():
    """Muestra el menú de opciones."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Calculadora de Funciones")
    print("------------------------")
    print("1: Graficar f(x) = x^3 + x")
    print("2: Salir")

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            try:
                xi, xf, n = obtener_datos_usuario()
                libf.plotf(f, xi, xf, n)
                input("Presione Enter para continuar...")
            except Exception as e:
                print(f"Error al graficar: {e}")
                input("Presione Enter para continuar...")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()