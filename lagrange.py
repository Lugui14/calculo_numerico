def lagrange_interpolation(points: list[tuple[float, float]]) -> callable[[float], float]:
	"""
	Generates an interpolating polynomial using the Lagrange method.

	The function returns another function (a closure) that represents the
	interpolating polynomial P(x), which can then be evaluated at any point x.

	Args:
		points: A list of tuples with the coordinates (x, y) of the points.

	Returns:
		A function that represents the polynomial P(x).
	"""
     
	x_points = [p[0] for p in points]
	y_points = [p[1] for p in points]

	def P(x: float) -> float:
		"""
		Evaluates the interpolating polynomial P at the point x.
		"""
		total_sum = 0
		for j in range(len(x_points)):
			# Start calculating the j-th Lagrange basis polynomial L_j(x)
			basis_polynomial = 1
			for i in range(len(x_points)):
				if i == j:
					continue

				# Multiply the terms (x - x_i) / (x_j - x_i)
				basis_polynomial *= (x - x_points[i]) / (x_points[j] - x_points[i])

			# Add the term y_j * L_j(x) to the total
			total_sum += y_points[j] * basis_polynomial

		return total_sum

	return P