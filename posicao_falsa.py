def false_position_method(f: callable, a: float, b: float, tol=1e-6, max_iter=100) -> float:
    """
    Find a root of f(x)=0 in [a, b] using the false position method.
    Args:
        f: function to find root of
        a: left endpoint
        b: right endpoint
        tol: tolerance for stopping
        max_iter: maximum number of iterations
    Returns:
        Approximate root or None if no root found
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iter):
        c = (a * abs(f(b)) + b * abs(f(a))) / (abs(f(b)) + abs(f(a)))
        if abs(f(c)) < tol or abs(b - a) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
    return (a * f(b) + b * f(a)) / (f(b) - f(a))  # Final approximation if max_iter reached

a = float(input("Enter left endpoint a: "))
b = float(input("Enter right endpoint b: "))
tol = float(input("Enter tolerance (e.g., 1e-6): "))

f = lambda x: x**3 - 9*x + 3  # Example function, replace with your own

print(f"False position method root: {false_position_method(f, a, b, tol)}")