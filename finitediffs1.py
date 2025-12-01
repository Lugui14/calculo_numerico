def fatorial(n: int) -> int:
    """
	Computes the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def finite_diffs(points: list[tuple[float, float]]) -> callable:
    """
    Computes the Newton-Gregory finite differences table and returns a function that represents
    the Newton interpolating polynomial.

    Args:
            points: A list of tuples with the coordinates (x, y) of the points.

    Returns:
            A function that represents the Newton-Gregory interpolating polynomial.
    """

    x_points = [p[0] for p in points]
    y_points = [p[1] for p in points]
    space_x = x_points[1] - x_points[0]

    def P(x: float) -> float:
        """
        Evaluates the Newton-Gregory interpolating polynomial P at the point x.
        """
        y0 = y_points[0]
        deltaiy = [[] for _ in range(len(points))]
        deltaiy[0] = y_points[:]

        for i in range(1, len(points)):
            for j in range(len(deltaiy[i - 1]) - 1):
                div = (deltaiy[i - 1][j + 1] - deltaiy[i - 1][j])
                deltaiy[i].append(div)

        asum = y0
        z = (x - x_points[0])/space_x
        for i in range(1, len(points)):
            mult = 1
            for j in range(i):
                mult *= z - j
            asum += mult * (deltaiy[i][0]/fatorial(i))
        return asum

    return P


polinomium = finite_diffs(
    [(-1, -11), (0, 1), (1, 3), (2, 1)]
)

polinomium2 = finite_diffs(
	[(2, 0.693), (3, 1.099), (4, 1.386)]
)

print(polinomium(5))
print(polinomium2(3.8))
