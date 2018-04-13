from scipy.sparse.linalg import spsolve
from oppgave2 import lagA


def y_approx_vector():
    n = 10
    E = 1.3 * 10 ** 10  # N/m^2
    I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12
    h = 2 / n  # h = L/n, der L = 2.0 meter
    # f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
    f = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m
    b = [(h ** 4 / (E * I)) * f] * n

    A = lagA(n)
    y_c = spsolve(A, b)
    return y_c


if __name__ == "__main__":
    y_c = y_approx_vector()
    print("y_c:\n", y_c)
