from fractions import Fraction

import scipy as sp
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix


def lagA(n):
    e = sp.ones(n)
    A = spdiags([e, -4.0*e, 6.0*e, -4.0*e, e], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    B = csr_matrix([[16.0, -9.0, (8/3), (-1/4)],
                   [(16/17), (-60/17), (72/17), (-28/17)],
                   [(-12/17), (96/17), (-156/17), (72/17)]])

    A[0, 0: 4] = B[0, :]
    A[n-2, n-4: n] = B[1, :]
    A[n-1, n-4: n] = B[2, :]

    return A


if __name__ == "__main__":
    a = lagA(10)
    print(a.todense())

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            print(a[i, j], end="\t")
        print()
