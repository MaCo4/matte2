from numpy import matrix
from numpy.linalg import solve
from math import sqrt


def gauss_newton(x0: matrix, r, Dr, iterations: int):
    x = x0

    for i in range(iterations):
        A = Dr(x)
        s = solve(A.T * A, -(A.T * r))
        x = x + s


if __name__ == "__main__":
    def r(v: matrix) -> matrix:
        x, y = v[0, 0], v[1, 0]
        return matrix([
            [sqrt(x**2 + (y - 1)**2) - 1],
            [sqrt((x - 1)**2 + (y - 1)**2) - 1],
            [sqrt(x**2 + (y + 1)**2) - 1]
        ])

    def Dr(v: matrix) -> matrix:
        x, y = v[0, 0], v[1, 0]
        return matrix([

        ])


    gauss_newton(matrix([[0], [0]]), r, Dr, iterations=1)
