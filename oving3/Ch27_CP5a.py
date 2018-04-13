from numpy import matrix
from Ch27_CP3 import newton_multivariate


if __name__ == "__main__":
    def F(v: matrix):
        x, y, z = v[0, 0], v[1, 0], v[2, 0]
        return matrix([
            [(x - 1)**2 + (y - 1)**2 + z**2 - 1],
            [(x - 1)**2 + y**2 + (z - 1)**2 - 1],
            [x**2 + (y - 1)**2 + (z - 1)**2 - 1]
        ])

    def DF(v: matrix):
        x, y, z = v[0, 0], v[1, 0], v[2, 0]
        return matrix([
            [2 * x - 2, 2 * y - 2, 2 * z],
            [2 * x - 2, 2 * y, 2 * z - 2],
            [2 * x, 2 * y - 2, 2 * z - 2]
        ])


    iterations = 10
    print("Punkt 1 med start i [0, 0, 0]:\n", newton_multivariate(matrix([[0], [0], [0]]), F, DF, iterations))
    print("\nPunkt 2 med start i [1, 1, 1]:\n", newton_multivariate(matrix([[1], [1], [1]]), F, DF, iterations))
