import math

def secant_method(f: callable, a: float, b: float, tol: float = 1e-7, max_iter: int = 100):
	"""
	Perform secant's method to find a root of the function f.

	Parameters:
	f (callable): The function for which we want to find the root.
	a (float): First initial guess for the root.
	b (float): Second initial guess for the root.
	tol (float): Tolerance for convergence.
	max_iter (int): Maximum number of iterations.

	Returns:
	float: Approximation of the root.
	"""
	x0 = b
	x1 = (a + b) / 2.0

	for _ in range(max_iter):
		aux = x1
		x1 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
		x0 = aux

		if abs(x1 - x0) < tol:
			break

	return x1

a = float(input("Enter initial guess a: "))
b = float(input("Enter second guess b: "))
tol = float(input("Enter tolerance (e.g., 1e-6): "))
f = lambda x: x*math.log10(x) - 1 # Example function, replace with your own

print(f"Secant's method root: {secant_method(f, a, b, tol)}")