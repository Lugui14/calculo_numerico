def euler_method(function: callable, first_value: tuple[float, float], iterations: int, domain: tuple[float, float]) -> list[tuple[float, float]]:
    """
    Approximates the solution of a first-order ordinary differential equation
    using Euler's numerical method.

    The function computes successive estimates of y over the given domain,
    starting from an initial point (x0, y0) and applying the update
    y_{n+1} = y_n + h * f(x_n, y_n), where h is the step size.

    Args:
        function: A callable f(x, y) defining the differential equation y' = f(x, y).
        first_value: A tuple (x0, y0) representing the initial condition.
        iterations: The number of Euler steps to perform.
        domain: A tuple (a, b) specifying the interval over which to approximate.

    Returns:
        A list of (x, y) tuples representing the approximate solution at each step.
    """
    y_values = []
    h = (domain[1] - domain[0])/iterations

    xi = first_value[0]
    y_values.append([xi,first_value[1]])
    for i in range(iterations):
        yi = y_values[i][1] + h* function(xi, y_values[i][1])
        y_values.append([xi+h,yi])
        xi += h
    
    return y_values

g = lambda x, y: x+y    #Function
start = [0,1]           #[x, f(x)] f' = g
n = 5                   #Number of Iterations
x = [0,1]               #Domain, [0,1] -> between 0 and 1
print(euler_method(g, start, n, x))