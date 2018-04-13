from numpy import matrix
from Ch27_CP3 import newton_multivariate


if __name__ == "__main__":
    def F(v: matrix):
        x, y, z = v[0, 0], v[1, 0], v[2, 0]
        return matrix([
            [(x - 1)**2 + (y + 2)**2 + z**2 - 25],
            [(x + 2)**2 + (y - 2)**2 + (z + 1)**2 - 25],
            [(x - 4)**2 + (y + 2)**2 + (z - 3)**2 - 25]
        ])

    def DF(v: matrix):
        x, y, z = v[0, 0], v[1, 0], v[2, 0]
        return matrix([
            [2 * x - 2, 2 * y + 4, 2 * z],
            [2 * x + 4, 2 * y - 4, 2 * z + 2],
            [2 * x - 8, 2 * y + 4, 2 * z - 6]
        ])


    iterations = 15
    print("Punkt 1 med start i [-2, -2, -2]:\n", newton_multivariate(matrix([[-2], [-2], [-2]]), F, DF, iterations))
    print("\nPunkt 2 med start i [2, 2, 2]:\n", newton_multivariate(matrix([[2], [2], [2]]), F, DF, iterations))
