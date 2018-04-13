from numpy import matrix
from numpy.linalg import solve


def newton_multivariate(x0: matrix, F, DF, iterations: int) -> matrix:
    x = x0

    for i in range(iterations):
        s = solve(DF(x), -F(x))
        x = x + s

    return x


if __name__ == "__main__":
    def F(x: matrix) -> matrix:
        u, v = x[0, 0], x[1, 0]
        return matrix([
            [u**3 - v**3 + u],
            [u**2 + v**2 - 1]
        ])

    def DF(x: matrix) -> matrix:
        u, v = x[0, 0], x[1, 0]
        return matrix([
            [3 * u**2 + 1, -3 * v**2],
            [2 * u, 2 * v]
        ])


    iterations = 10
    print("Løsning 1 med start x=[1, 1]:\n", newton_multivariate(matrix([[1], [1]]), F, DF, iterations))
    print("\nLøsning 2 med start x=[-1, -1]:\n", newton_multivariate(matrix([[-1], [-1]]), F, DF, iterations))
