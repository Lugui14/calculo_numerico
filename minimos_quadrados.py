def least_squares(point_list : list[tuple[float, float]]) -> callable:
    """
    Generates the best-fitting line for a set of data points by minimizing the sum of the squares of the errors

	The function returns another function (a closure) that represents a
	line, by the function f(x) = a + b*x, which can then be evaluated at any point x.

	Args:
		point_list: A list of tuples with the coordinates (x, y) of the points.

	Returns:
		A function that represents the line function: f(x) = a + b*x.
    """
    list_size = len(point_list)
    sum_x = sum_x_sq = sum_y = sum_y_sq = sum_x_times_y = 0

    for i in range(list_size):
        sum_x += point_list[i][0]
        sum_x_sq += point_list[i][0]*point_list[i][0]

        sum_y += point_list[i][1]
        sum_y_sq += point_list[i][1]*point_list[i][1]

        sum_x_times_y += point_list[i][0]*point_list[i][1]
    
    b = ( list_size*sum_x_times_y - sum_x*sum_y ) / ( list_size*sum_x_sq - sum_x*sum_x )
    a = ( sum_y - b*sum_x ) / list_size
    #print(f"y = {a} + {b}*x")

    r_sq = (( list_size*sum_x_times_y - sum_x*sum_y )**2 ) / ( ( list_size*sum_x_sq - sum_x*sum_x )*( list_size*sum_y_sq - sum_y*sum_y ) )
    #print(f"R² = {r_sq}")

    return lambda x: a + b*x

lista = [(1,0.5),(2,2.5),(3,2),(4,4),(5,3.5),(6,6),(7,5.5)]
least_squares(lista)