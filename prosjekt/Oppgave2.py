import scipy as sp
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix


# INPUT: n, størrelsen på matrisen
def lagA(n):
    e = sp.ones(n)
    # Definerer båndmatrisen
    A = spdiags([e, -4.0 * e, 6.0 * e, -4.0 * e, e], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    # Definerer første, nest siste og siste rad i matrisen
    B = csr_matrix([[16.0, -9.0, (8 / 3), (-1 / 4)],
                    [(16 / 17), (-60 / 17), (72 / 17), (-28 / 17)],
                    [(-12 / 17), (96 / 17), (-156 / 17), (72 / 17)]])

    # Bytter de fire første tallene på første rad i matrise A, med første rad i matrise B
    A[0, 0: 4] = B[0, :]
    # Bytter de fire siste tallene på nest siste rad i matrise A, med den midterste raden i matrise B
    A[n - 2, n - 4: n] = B[1, :]
    # Bytter de fire siste tallene på siste rad i matrise A, med siste rad i matrise B
    A[n - 1, n - 4: n] = B[2, :]

    return A
