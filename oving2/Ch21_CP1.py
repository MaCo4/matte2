from numpy import matrix, finfo, zeros


def gaussian_elim_solve(a: matrix, b: matrix):
    """
    Gaussian elimination of a matrix and solving of Ax = b.

    :param a: the coefficient matrix
    :type a: matrix
    :param b: the "b" column vector
    :type b: matrix
    :return: a column vector "x" of the unknowns
    :rtype: matrix
    """

    rows, cols = a.shape
    assert rows == cols  # Pass på at koeffisientmatrisen er kvadratisk

    # Itererer søylene bortover fra venstre til høyre, der pivotelementene skal være.
    # j representerer rad- og søylenummer der vi skal lage pivotelement
    for j in range(0, rows - 1):

        if abs(a[j, j]) < finfo(float).eps:
            print("Zero pivot encountered at [{},{}]".format(j, j))
            return

        for i in range(j + 1, rows):  # Itererer radene under nåværende pivot. i er raden vi skal eliminere nå

            mult = a[i, j] / a[j, j]  # Elementet under pivotelementet delt på pivotelementet

            for k in range(j, rows):  # Itererer bortover rad i fom. element [i,j], eliminerer elementet [i,k]
                a[i, k] = a[i, k] - mult * a[j, k]

            b[i] = b[i] - mult * b[j]

    x = zeros((rows, 1))
    c = b.copy()
    for i in range(rows - 1, -1, -1):
        for j in range(i + 1, rows):
            c[i] = c[i] - a[i, j] * x[j]
        x[i] = c[i] / a[i, i]

    return x


if __name__ == "__main__":  # Testing under utviklingen
    a = matrix([[1, 3, 5],
                [2, 4, 6],
                [2, 3, 5]])
    b = matrix([[7],
                [8],
                [7]])
    print(a, "\n", b)
    x = gaussian_elim_solve(a, b)
    print("\nEtter Gaussing:")
    print(a, "\n", b, "\n\n", x)
