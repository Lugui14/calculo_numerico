import math
import re


def trapezoidal_method(f: callable, a: float, b: float, n: int) -> float:
    """
    Approximate the integral of f from a to b using the trapezoidal rule with n subintervals.

    Parameters:
    f : callable
            The integrand function.
    a : float
            The lower limit of integration.
    b : float
            The upper limit of integration.
    n : int
            The number of subintervals.

    Returns:
    float
            The approximate value of the integral.
    """
    h = (b - a) / n
    trapezio_f = lambda a, b: (f(a) + f(b))
    integral = 0

    for i in range(n):
        integral += trapezio_f(a + (i * h), a + ((i + 1) * h))

    return integral * (h / 2)


# Definindo a função a ser integrada
def func(x):
    return (x**2 * math.cos(x)) / math.e**x


# Definindo os limites de integração e o número de subintervalos
a = 0
b = 2
n = 10000

# Calculando a integral aproximada
resultado = trapezoidal_method(func, a, b, n)
print(f"A integral aproximada de (x^2 * cos(x)) / e^x) de {a} a {b} é: {resultado}")
