def runge_kutta_2nd_order(
    function: callable, first_value: tuple[float, float], iterations: int, domain: tuple[float, float]
) -> list[tuple[float, float]]:
    """
    Approximates the solution of a first-order ordinary differential equation (ODE)
    using the second-order Runge–Kutta method (also known as RK2 or Heun’s method).

    This algorithm improves on Euler's method by evaluating the slope twice
    at each iteration—first at the beginning of the interval (k1), then at an
    estimated endpoint (k2). The final slope is the average of these two,
    producing a more accurate approximation.

    Args:
        function: A callable f(x, y) representing the derivative dy/dx.
        first_value: A tuple (x0, y0) representing the initial condition.
        iterations: Number of RK2 steps to perform.
        domain: A tuple (a, b) defining the interval over which to approximate the solution.

    Returns:
        A list of (x, y) tuples representing the approximate solution at each step.
    """
    y_values = []
    h = (domain[1] - domain[0]) / iterations

    k1 = lambda x, y: h * function(x, y)
    k2 = lambda x, y, k: h * function(x + h, y + k)

    xi = first_value[0]
    y_values.append([xi, first_value[1]])
    for i in range(iterations):
        k1i = k1(xi, y_values[i][1])
        k2i = k2(xi, y_values[i][1], k1i)

        yi = y_values[i][1] + 0.5 * (k1i + k2i)
        y_values.append([xi + h, yi])
        xi += h

    return y_values


def runge_kutta_4nd_order(
    function: callable, first_value: tuple[float, float], iterations: int, domain: tuple[float, float]
) -> list[tuple[float, float]]:
    """
    Approximates the solution of a first-order ordinary differential equation (ODE)
    using the classical fourth-order Runge–Kutta method (RK4).

    RK4 is one of the most widely used numerical methods for solving ODEs because
    it provides high accuracy without requiring extremely small step sizes.
    The method evaluates the slope four times per iteration (k1, k2, k3, k4),
    combining them in a weighted average to estimate the next value of y.

    Args:
        function: A callable f(x, y) representing the derivative dy/dx.
        first_value: A tuple (x0, y0) representing the initial condition.
        iterations: Number of RK4 steps to perform.
        domain: A tuple (a, b) defining the interval over which to approximate the solution.

    Returns:
        A list of (x, y) tuples representing the approximate solution at each step.
    """
    y_values = []
    h = (domain[1] - domain[0]) / iterations

    k1 = lambda x, y: h * function(x, y)
    k2 = lambda x, y, k: h * function(x + h / 2, y + k / 2)
    k3 = lambda x, y, k: h * function(x + h / 2, y + k / 2)
    k4 = lambda x, y, k: h * function(x + h, y + k)

    xi = first_value[0]
    y_values.append([xi, first_value[1]])
    for i in range(iterations):
        k1i = k1(xi, y_values[i][1])
        k2i = k2(xi, y_values[i][1], k1i)
        k3i = k3(xi, y_values[i][1], k2i)
        k4i = k4(xi, y_values[i][1], k3i)

        yi = y_values[i][1] + (1 / 6) * (k1i + 2 * k2i + 2 * k3i + k4i)
        y_values.append([xi + h, yi])
        xi += h

    return y_values


g = lambda x, y: -x+y+2  # Function
start = [0, 2]  # [x, f(x)] f' = g
n = 10  # Number of Iterations
x = [0, 1]  # Domain, [1,2] -> between 1 and 2
print(runge_kutta_2nd_order(g, start, n, x))
print(runge_kutta_4nd_order(g, start, n, x))
