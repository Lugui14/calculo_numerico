def gauss_method(fs: list):
	"""
	Solve a system of linear equations using Gaussian elimination.
	
	With roundings to 4 decimal places during elimination and 2 decimal places in the final result.

	Parameters:
	fs (list): List of lists representing the augmented matrix of the system.

	Returns:
	list: Solution vector.
	"""

	lenA = len(fs) -1

	for i in range(lenA):
		for j in range(i+1, lenA+1):
			m = fs[j][i]/fs[i][i]

			for k in range(i, lenA+1):
				fs[j][k] -= m*fs[i][k]

			fs[j][-1] -= m*fs[i][-1]

	for i in range(lenA+1):
		for j in range(lenA+2):
			fs[i][j] = round(fs[i][j], 4)
					
	res = [0]*(lenA+1)
	res[-1] = fs[-1][-1]/fs[-1][-2]

	for i in range(lenA, -1, -1):
		soma = 0
		for j in range(i+1, lenA+1):
			soma += fs[i][j]*res[j]

		res[i] = (fs[i][-1] - soma)/fs[i][i]

	for i in range(lenA+1):
		res[i] = round(res[i], 2)
	
	return res

print(gauss_method([[3,2,1,5],[1,1,2,3],[2,3,-2,-1]]))

