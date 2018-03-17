from math import inf
from scipy.sparse.linalg import spsolve, inv, norm
from oppgave2 import lagA


def solve(A, b):
    y = spsolve(A, b)
    s = y.shape
    return y[s[0] - 1]


if __name__ == "__main__":
    E = 1.3 * 10 ** 10  # N/m^2
    I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12
    # f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
    fx = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m

    for i in range(1, 12):
        n = 10 * 2 ** i
        h = 2 / n  # h = L/n, der L = 2.0 meter
        b = [(h ** 4 / (E * I)) * fx] * n
        y2 = fx / (24 * E * I) * 2 ** 2 * (2 ** 2 - 4 * 2 * 2 + 6 * 2 ** 2)
        A = lagA(n)
        AI = inv(A)
        print("Eksponent: {}, n = {}".format(i, n))
        print("Kondisjonstall: ", norm(A, ord=inf) * norm(AI, ord=inf))
        print("y: ", y2 - solve(A, b), "\n")
