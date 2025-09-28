def remove_float_point(num: float, tolerance: float = 1e-4) -> float:
	"""
	Remove floating point inaccuracies by rounding to the nearest integer if within a specified tolerance.

	Parameters:
	num (float): The number to be processed.
	tolerance (float): The tolerance level for rounding.

	Returns:
	float: The processed number, rounded if within tolerance.
	"""
	if abs(num - round(num)) < tolerance:
		return round(num)
	return num

def jacobi_method(fs: list, max_iterations: int = 100, tolerance: float = 1e-4):
	"""
	Solve a system of linear equations using the Jacobi method.

	With roundings to 4 decimal places during elimination and 2 decimal places in the final result.

	Parameters:
	fs (list): List of lists representing the augmented matrix of the system.
	max_iterations (int): Maximum number of iterations to perform.
	tolerance (float): Tolerance for convergence.

	Returns:
	list: Solution vector.
	"""

	matrixA = [row[:-1] for row in fs]
	listB = [row[-1] for row in fs]
	
	rows = len(matrixA)
	cols = len(matrixA[0])

	vector = [0 for _ in range(rows)]

	_ = 0
	while True:
		if _ >= max_iterations:
			return [remove_float_point(val) for val in new_vector]

		new_vector = vector.copy()
		for i in range(rows):
			sum_ax = listB[i]
			for j in range(cols):
				if i != j:
					sum_ax -= matrixA[i][j] * vector[j]
			new_vector[i] = sum_ax / matrixA[i][i]

		if max(abs(new_vector[i] - vector[i]) for i in range(rows)) < tolerance:
			return [remove_float_point(val) for val in new_vector]

		vector = new_vector
		_ += 1

print(jacobi_method([[5,-1,2,2,3],[2,-4,1,-1,-2],[1,2,4,1,6],[-1,1,2,6,4]]))
#print(jacobi_method([[3,2,1,5],[1,1,2,3],[2,3,-2,-1]])) #<- Não converge
#print(jacobi_method([[1,1,3],[1,-3,-3]]))
