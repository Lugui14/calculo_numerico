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

def gauss_method(fs: list):
	"""
	Solve a system of linear equations using Gaussian elimination.
	
	With roundings to 4 decimal places during elimination and 2 decimal places in the final result.

	Parameters:
	fs (list): List of lists representing the augmented matrix of the system.

	Returns:
	list: Solution vector.
	"""

	matrixA = [row[:-1] for row in fs]
	listB = [row[-1] for row in fs]
	
	rows = len(matrixA)
	cols = len(matrixA[0])

	for i in range(rows):
		pivot = matrixA[i][i]
		for j in range(i + 1, rows):
			m = remove_float_point(matrixA[j][i] / pivot)
			listB[j] = remove_float_point(listB[j] - m * listB[i])

			for k in range(i, cols):
				matrixA[j][k] = remove_float_point(matrixA[j][k] - m * matrixA[i][k])

	results = listB[:]

	for i in range(rows-1, -1, -1):
		for j in range(i + 1, rows):
			results[i] = remove_float_point(results[i] - matrixA[i][j] * results[j])
		results[i] = remove_float_point(results[i] / matrixA[i][i])

	return results

if __name__ == '__main__':
    print(gauss_method([[3,2,4,1],[1,1,2,2],[4,3,-2,3]]))