from numpy import matrix, zeros
from Ch22_CP1 import lu_factorize


def lu_solve(a: matrix, b: matrix):
    l, u = lu_factorize(a)
    rows, cols = l.shape

    # Løser først Lc = b for c
    c = zeros((rows, 1))
    b = b.copy()
    for i in range(rows):
        for j in range(i):
            b[i] = b[i] - l[i, j] * c[j]
        c[i] = b[i] / l[i, i]

    # Løser dermed Ux = c for x
    x = zeros((rows, 1))
    for i in range(rows - 1, -1, -1):
        for j in range(i + 1, rows):
            c[i] = c[i] - u[i, j] * x[j]
        x[i] = c[i] / u[i, i]

    return x


if __name__ == "__main__":
    a = matrix([[3, 1, 2],  # Matrisen fra oppgave 4a
                [6, 3, 4],
                [3, 1, 5]])

    b = matrix([[0],
                [1],
                [3]])

    print("Matrisen fra oppgave 4a:\nA=\n", a)
    print("\nb-vektoren:\n", b)
    x = lu_solve(a, b)
    print("\nx=\n", x)
