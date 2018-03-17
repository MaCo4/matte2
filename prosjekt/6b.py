import scipy as sp
import math as m
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as mpl


def lagA(n):
    e = sp.ones(n)
    A = spdiags([e, -4.0 * e, 6.0 * e, -4.0 * e, e], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    B = csr_matrix([[16.0, -9.0, (8 / 3), (-1 / 4)],
                    [(16 / 17), (-60 / 17), (72 / 17), (-28 / 17)],
                    [(-12 / 17), (96 / 17), (-156 / 17), (72 / 17)]])

    A[0, 0: 4] = B[0, :]
    A[n - 2, n - 4: n] = B[1, :]
    A[n - 1, n - 4: n] = B[2, :]
    return A


def solve(A, b):
    y = spsolve(A, b)
    s = y.shape
    f = y[s[0] - 1]
    return y[s[0] - 1]


E = 1.3 * 10 ** 10  # N/m^2
I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12
# f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
fx = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m
sx = -9.81 * 100 * m.sin(m.pi * 2 / 2)

for i in range(1, 12):
    n = 10 * 2 ** i
    print(i)
    h = 2 / n  # h = L/n, der L = 2.0 meter
    b = [(h ** 4 / (E * I)) * (fx + sx)] * n
    y2 = fx / (24 * E * I) * 2 ** 2 * (2 ** 2 - 4 * 2 * 2 + 6 * 2 ** 2) - 9.81 * 100 * 2 / (E * I * m.pi) * (
    2 ** 3 / m.pi ** 3 * m.sin(m.pi * 2 / 2) - 2 ** 3 / 6 + 2 * 2 ** 2 / 2 - 2 ** 2 * 2 / m.pi)
    A = lagA(n)
