from sympy import diff, symbols

def newton_method(f: callable, x0: float, tol: float = 1e-7, max_iter: int = 100):
	"""
	Perform Newton's method to find a root of the function f.

	Parameters:
	f (callable): The function for which we want to find the root.
	x0 (float): Initial guess for the root.
	tol (float): Tolerance for convergence.
	max_iter (int): Maximum number of iterations.

	Returns:
	float: Approximation of the root.
	"""
	x_symbol = symbols('x')
	f_prime = diff(f(x_symbol), x_symbol)

	for _ in range(max_iter):
		f_xn = f(x0)
		f_prime_xn = f_prime.subs(x_symbol, x0)
		
		if f_prime_xn == 0:
			raise ValueError("Derivative is zero. No solution found.")
		
		x0 = x0 - (f_xn / f_prime_xn)

		if abs(f_xn) < tol:
			return x0

	return x0

a = float(input("Enter initial guess x0: "))
tol = float(input("Enter tolerance (e.g., 1e-6): "))
f = lambda x: x**2 - 7  # Example function, replace with your own

print(f"Newton's method root: {newton_method(f, a, tol)}")