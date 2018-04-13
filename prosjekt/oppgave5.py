from math import inf, log
import matplotlib.pyplot as plot
from scipy.sparse.linalg import spsolve, inv, norm
from oppgave2 import lagA


if __name__ == "__main__":
    E = 1.3 * 10 ** 10  # N/m^2
    I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12

    # f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
    fx = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m

    cond = []
    err = []

    for i in range(1, 11):
        n = 10 * 2 ** i
        h = 2 / n  # h = L/n, der L = 2.0 meter
        b = [(h ** 4 / (E * I)) * fx] * n

        # Eksakt verdi for y(2.0)
        y2 = fx / (24 * E * I) * 2 ** 2 * (2 ** 2 - 4 * 2 * 2 + 6 * 2 ** 2)

        A = lagA(n)
        AI = inv(A)

        condition = norm(A, ord=inf) * norm(AI, ord=inf)
        cond.append(log(condition))

        y = spsolve(A, b)
        error = y2 - y[n - 1]
        err.append(log(abs(error)))

        print("Eksponent: {}, n = {}".format(i, n))
        print("Kondisjonstall: ", condition)
        print("Feil i x=L: ", error, "\n")

    plot.plot(cond)
    plot.plot(err)
    plot.show()
