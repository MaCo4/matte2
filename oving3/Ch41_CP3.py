from numpy import matrix, ones
from numpy.linalg import solve
from math import sqrt


def least_squares_line(x, y):
    A = matrix(ones((len(x), 2)))
    for i, x in enumerate(x):
        A[i, 1] = x

    b = matrix(ones((len(y), 1)))
    for i, y in enumerate(y):
        b[i, 0] = y

    c = solve(A.T * A, A.T * b)

    return {"A": A, "b": b, "c": c}


def least_squares_parabola(x, y):
    A = matrix(ones((len(x), 3)))
    for i, x in enumerate(x):
        A[i, 1] = x
        A[i, 2] = x**2

    b = matrix(ones((len(y), 1)))
    for i, y in enumerate(y):
        b[i, 0] = y

    c = solve(A.T * A, A.T * b)

    return {"A": A, "b": b, "c": c}


if __name__ == "__main__":
    x = [1960, 1970, 1990, 2000]
    y = [3039585530, 3707475887, 5281653820, 6079603571]

    line = least_squares_line(x, y)
    parabola = least_squares_parabola(x, y)

    y_line = lambda x: line['c'][0, 0] + line['c'][1, 0] * x
    y_parabola = lambda x: parabola['c'][0, 0] + parabola['c'][1, 0] * x + parabola['c'][2, 0] * x**2

    print("y_line(1980) = {}".format(y_line(1980)))
    print("y_parabola(1980) = {}".format(y_parabola(1980)))

    r_line: matrix = line['b'] - line['A'] * line['c']
    r_parabola: matrix = parabola['b'] - parabola['A'] * parabola['c']

    RMSE_line = sqrt(sum(map(lambda r: r**2, r_line)) / r_line.size)
    RMSE_parabola = sqrt(sum(map(lambda r: r**2, r_parabola)) / r_parabola.size)
    print("RMSE line: {}, RMSE parabola: {}".format(RMSE_line, RMSE_parabola))
