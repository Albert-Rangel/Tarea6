import numpy as np
import matplotlib.pyplot as plt

def plotf(f, xi, xf, n):
    """
    Grafica una función dada en un intervalo especificado.

    Args:
        f: La función a graficar.
        xi: Límite inferior del intervalo.
        xf: Límite superior del intervalo.
        n: Número de puntos a graficar.
    """

    # Genera n puntos equidistantes en el intervalo
    x = np.linspace(xi, xf, n)

    # Evalúa la función en cada punto
    y = f(x)

    # Crea la gráfica
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfica de f(x)')
    plt.grid(True)
    plt.show()