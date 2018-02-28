from numpy import matrix, finfo


def gauss(mat: matrix):
    rows, cols = mat.shape  # Get size of matrix

    for j in range(0, cols - 1):  # Iterates through
        if abs(mat[j, j]) < finfo(float).eps:
            print("Zero pivot encountered!")
            return

        for i in range(j + 1, cols):
            mult = mat[i, j] / mat[j, j]
            for k in range(j + 1, cols):
                mat[i, k] = mat[i, k] - mult * mat[j, k]

            mat[i, cols - 1] = mat[i, cols - 1] - mult * mat[j, cols - 1]


if __name__ == "__main__":
    a = matrix([[1, 2, 3],
                [3, 4, 5],
                [5, 6, 7]])
    print(a)
    gauss(a)
    print("\nEtter Gaussing:")
    print(a)
