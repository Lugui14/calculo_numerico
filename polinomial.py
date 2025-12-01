from seidel import seidel_method

def matrix_mult(A, B):
    """
    Multiplies two matrices A and B using standard matrix multiplication.

    Args:
        A: A list of lists representing matrix A (m x n).
        B: A list of lists representing matrix B (n x p).

    Returns:
        A list of lists representing the product matrix C (m x p),
        where each entry C[i][j] = sum(A[i][k] * B[k][j] for k in range(n)).
    """
    C = []
    for row in A:
        temp = []
        for col in zip(*B):
            temp.append(sum(a*b for a, b in zip(row, col)))
        C.append(temp)
    return C

def polinomial(point_list : list[list[float]], degree) -> callable:
    """
    Computes a polynomial regression model of a specified degree for a set of
    data points and returns the resulting polynomial as a function.

    Args:
        point_list: A list of points, each given as [x, y].
        degree: The degree of the polynomial to fit.

    Returns:
        A callable representing the polynomial function f(x) that evaluates
        the fitted polynomial at any given value of x.
    """
    matrix_x = []
    matrix_x_transposed = []
    matrix_y = []
    row = len(point_list)
    col = len(point_list[0])-1

    for i in range(row):
        aux = [1]
        for j in range(degree):
            aux.append(point_list[i][0]**(j+1))
        matrix_x.append(aux)

    for i in range(degree+1):
        aux = []
        for j in range(row):
            aux.append(matrix_x[j][i])
        matrix_x_transposed.append(aux)
    
    for i in range(row):
        matrix_y.append([point_list[i][-1]])

    matrix_x_times_xt = matrix_mult(matrix_x_transposed, matrix_x)
    result = matrix_mult(matrix_x_transposed, matrix_y)

    new_matrix = []
    for i in range(len(matrix_x_times_xt)):
        aux = []
        for j in range(len(matrix_x_times_xt[0])):
            aux.append(matrix_x_times_xt[i][j])
        aux.append(result[i][0])
        new_matrix.append(aux)

    b_values = seidel_method(new_matrix)
    #print(b_values)
    return lambda x: b_values[0] + sum(
        b_values[i+1] * x**i for i in range(len(b_values))
    )

lista = [[-2,-30.5],[-1.5,-20.2],[0,-3.3],[1,8.9],[2.2,16.8],[3.1,21.4]]
polinomial(lista,2)