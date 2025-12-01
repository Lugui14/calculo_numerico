from gauss import gauss_method


def finite_diffs_method(
    f: list[callable],
    first_value: tuple[float, float],
    last_value: tuple[float, float],
    first_derivative: float,
    iterations: int,
    domain: tuple[float, float],
) -> list[tuple[float, float]]:
    """ """
    l = []
    h = (domain[1] - domain[0]) / iterations

    l.append(first_value)

    if first_derivative is not None:
        l.append([first_value[0] + h, first_value[1] + first_derivative * h])

        xi = l[-1][0]
        alfa = f[1](xi, h)
        beta = f[2](xi, h)
        gama = f[3](xi, h)
        for i in range(iterations - 1):
            xi = l[-1][0]
            yi = (f[0](xi, h) - beta * l[-1][1] - alfa * l[-2][1]) / gama
            l.append([xi + h, yi])

        return l

    matrix_ = []
    for i in range(iterations-1):
        aux = []
        xi = first_value[0] + (i + 1) * h
        
        alfa = f[1](xi, h)
        beta = f[2](xi, h)
        gama = f[3](xi, h)
        
        for j in range(iterations-1):
            if j == i:
                aux.append(beta)
            elif j == i - 1:
                aux.append(alfa)
            elif j == i + 1:
                aux.append(gama)
            else:
                aux.append(0)
        matrix_.append(aux)

    # Build right side vector
    b = []
    for i in range(iterations-1):
        xi = first_value[0] + (i + 1) * h
        fi_value = f[0](xi, h)

        if i == 0:
            fi_value -= alfa * first_value[1]
        if i == iterations - 2:
            fi_value -= gama * last_value[1]

        b.append(fi_value)

    for i in range(len(matrix_)):
        matrix_[i].append(b[i])

    solution = gauss_method(matrix_)

    result = [first_value]
    for i in range(len(solution)):
        xi = first_value[0] + (i + 1) * h
        result.append([xi, solution[i]])
    result.append(last_value)

    return result


# gama*y(i+1) + beta*yi + alfa*y(i-1) = F(xi)
# This values can be found by evalueting the starting function with
#   y'(xi) = ( y(i+1) - yi ) / h   or   ( y(i+1) - y(i-1) ) / 2h
#   y"(xi) = ( y(i+1) - 2yi + y(i-1) ) / h²

# Ex1, PVI
alfa = lambda x, h: 1
beta = lambda x, h: -2 - 2 * h + h * h
gama = lambda x, h: 1 + 2 * h
fi = lambda x, h: h * h * x

function_list = [fi, alfa, beta, gama]
first_value = [0, 2]
last_value = [None, None]  # Not known
first_derivative = 1
n = 5
domain = [0, 1]
print(finite_diffs_method(function_list, first_value, last_value, first_derivative, n, domain))

# Ex2, PVC
alfa = lambda x, h: 1 - h
beta = lambda x, h: -2 + h * h
gama = lambda x, h: 1 + h
fi = lambda x, h: h * h * x

function_list = [fi,alfa,beta,gama]
first_value = [0,2]
last_value = [1,0]
first_derivative = None #Not known
n = 4
domain = [0, 1]
print(finite_diffs_method(function_list, first_value, last_value, first_derivative, n, domain))
