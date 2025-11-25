import math


def simpson_method(f: callable, a: float, b: float, n: int) -> float:
    """
    Approximate the integral of f from a to b using Simpson's rule with n subintervals.

    Parameters:
    f : callable
                    The integrand function.
    a : float
                    The lower limit of integration.
    b : float
                    The upper limit of integration.
    n : int
                    The number of subintervals (must be even).

    Returns:
    float
                    The approximate value of the integral.
    """
    if n % 2 == 1:
        raise ValueError("Number of subintervals n must be even.")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        integral += 4 * f(a + i * h) if i % 2 == 1 else 2 * f(a + i * h)

    return integral * (h / 3)


# Definindo a função a ser integrada
def func(x):
    return (x**2 * math.cos(x)) / math.e**x


# Definindo os limites de integração e o número de subintervalos
a = 0
b = 2
n = 10000

# Calculando a integral aproximada
resultado = simpson_method(func, a, b, n)
print(f"A integral aproximada de (x^2 * cos(x)) / e^x) de {a} a {b} é: {resultado}")
