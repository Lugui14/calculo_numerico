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

def jordan_method(fs: list):
	"""
	Solve a system of linear equations using Jordan elimination.
	
	With roundings to 4 decimal places during elimination and 2 decimal places in the final result.

	Parameters:
	fs (list): List of lists representing the augmented matrix of the system.

	Returns:
	list: Solution vector.
	"""

	for i in range(len(fs)):

		pivot = fs[i][i]
		fs[i] = [val / pivot for val in fs[i]] # Transform the diagonal into ones

		for j in range(len(fs)): # Iterate rows to eliminate all other that not is the pivot
			if i != j: # Skip the pivot row
				factor = fs[j][i] # Get the factor to eliminate

				for k in range(i, len(fs[i])): # Iterate columns
					m = fs[i][k]
					fs[j][k] = fs[j][k] - factor * m # Zering the column

	return [remove_float_point(round(row[-1])) for row in fs]

print(jordan_method([[3,2,4,1],[1,1,2,2],[4,3,-2,3]]))