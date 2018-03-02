import sys
from numpy import matrix, zeros


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

        if abs(a[j, j]) < sys.float_info.min:
            print("Zero pivot encountered at [{},{}]. The value is {} and eps is {}".format(j, j, a[j, j], sys.float_info.min))
            # return

        for i in range(j + 1, rows):  # Itererer radene under nåværende pivot. i er raden vi skal eliminere nå

            mult = a[i, j] / a[j, j]  # Elementet under pivotelementet delt på pivotelementet

            for k in range(j, rows):  # Itererer bortover rad i fom. element [i,j], eliminerer elementet [i,k]
                a[i, k] = a[i, k] - mult * a[j, k]

            b[i] = b[i] - mult * b[j]

    x = zeros((rows, 1))
    b = b.copy()
    for i in range(rows - 1, -1, -1):
        for j in range(i + 1, rows):
            b[i] = b[i] - a[i, j] * x[j]
        x[i] = b[i] / a[i, i]

    return x


if __name__ == "__main__":  # Testing under utviklingen
    a = matrix([[2, -2, -1],
                [4, 1, -2],
                [-2, 1, -1]])
    b = matrix([[-2],
                [1],
                [-3]])

    print("Oppgave a:")
    print("A=\n", a, "\nb=\n", b)
    x = gaussian_elim_solve(a, b)
    print("x=\n", x)



    a = matrix([[1, 2, -1],
                [0, 3, 1],
                [2, -1, 1]])
    b = matrix([[2],
                [4],
                [2]])

    print("\nOppgave b:")
    print("A=\n", a, "\nb=\n", b)
    x = gaussian_elim_solve(a, b)
    print("x=\n", x)



    a = matrix([[2, 1, -4],
                [1, -1, 1],
                [-1, 3, -2]])
    b = matrix([[-7],
                [-2],
                [6]])

    print("\nOppgave c:")
    print("A=\n", a, "\nb=\n", b)
    x = gaussian_elim_solve(a, b)
    print("x=\n", x)
