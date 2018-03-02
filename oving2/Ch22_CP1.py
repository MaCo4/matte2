import sys
from numpy import matrix, identity


def lu_factorize(a: matrix):
    rows, cols = a.shape
    assert rows == cols  # Pass på at koeffisientmatrisen er kvadratisk

    l = identity(rows)
    u = a.copy()

    # Itererer søylene bortover fra venstre til høyre, der pivotelementene skal være.
    # j representerer rad- og søylenummer der vi skal lage pivotelement
    for j in range(0, rows - 1):

        if abs(u[j, j]) < sys.float_info.min:
            print("Zero pivot encountered at [{},{}]".format(j, j))
            return

        for i in range(j + 1, rows):  # Itererer radene under nåværende pivot. i er raden vi skal eliminere nå

            mult = u[i, j] / u[j, j]  # Elementet under pivotelementet delt på pivotelementet
            l[i, j] = mult

            for k in range(j, rows):  # Itererer bortover rad i fom. element [i,j], eliminerer elementet [i,k]
                u[i, k] = u[i, k] - mult * u[j, k]

    return l, u


if __name__ == "__main__":
    a = matrix([[4, 2, 0],  # Matrisen fra oppgave 2b
                [4, 4, 2],
                [2, 2, 3]])

    print("Matrisen fra oppgave 2b:\nA=\n", a)
    l, u = lu_factorize(a)
    print("Etter LU-faktorisering:")
    print("L=\n", l, "\nU=\n", u)
