def divided_diffs(points: list[tuple[float, float]]) -> callable:
    """
    Computes the Newton's divided differences table and returns a function that represents
    the Newton interpolating polynomial.

    Args:
            points: A list of tuples with the coordinates (x, y) of the points.

    Returns:
            A function that represents the Newton interpolating polynomial.
    """

    x_points = [p[0] for p in points]
    y_points = [p[1] for p in points]

    def P(x: float) -> float:
        """
        Evaluates the Newton interpolating polynomial P at the point x.
        """
        y0 = y_points[0]
        deltaiy = [[] for _ in range(len(points))]
        deltaiy[0] = y_points[:]

        for i in range(1, len(points)):
            for j in range(len(deltaiy[i - 1]) - 1):
                div = (deltaiy[i - 1][j + 1] - deltaiy[i - 1][j]) / (
                    x_points[j + i] - x_points[j]
                )
                deltaiy[i].append(div)

        # delta y table
        # print(deltaiy)

        asum = y0
        for i in range(len(points)):
            mult = 1
            for j in range(i):
                mult *= x - x_points[j]
            asum += mult * deltaiy[i][0]
        return asum

    return P


polinomium = divided_diffs(
    [(1, 2.75), (3, 8.3), (6, 15.6), (7, 17.9), (9, 22.4), (11, 26.8)]
)

print(polinomium(12))
print(polinomium(13))
