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

def mult_linear(point_list : list[list[float]]) -> callable:
    """
    Computes the multivariate linear regression model for a set of data points
    using the Normal Equation (XᵀX · b = Xᵀy), and returns the resulting 
    linear function as a closure.

    Args:
        point_list: A list of lists where each inner list contains the feature
            values followed by the corresponding output value.

    Returns:
        A callable representing the regression function f(*args) that evaluates
        the fitted linear model at any given input.
    """
    matrix_x = []
    matrix_x_transposed = []
    matrix_y = []
    row = len(point_list)
    col = len(point_list[0])-1

    for i in range(row):
        aux = [1]
        for j in range(col):
            aux.append(point_list[i][j])
        matrix_x.append(aux)
    
    for i in range(col+1):
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
    return lambda *args: b_values[0] + sum(
        b_values[i+1] * args[i] for i in range(len(args))
    )

lista = [[-1,-2,13],[0,-1,11],[1,0,9],[2,1,4],[4,1,11],[5,2,9],[5,3,1],[6,4,-1]]
mult_linear(lista)