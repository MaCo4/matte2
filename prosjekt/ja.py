from oppgave2 import lagA


def calculate(b):
    E = 1.3 * 10 ** 10  # N/m^2
    I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12
    L = 2
    # f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
    fx = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m
    y = [0.0] * 10
    for i in range(0, 10):
        x = b[i]
        y[i] = (fx / (24 * E * I)) * (x**2) * ((x**2) - (4 * L * x) + (6 * (L**2)))
    return y


if __name__ == "__main__":
    b = [0.0] * 10
    b[0] = 0.2
    b[1] = 0.4
    b[2] = 0.6
    b[3] = 0.8
    b[4] = 1.0
    b[5] = 1.2
    b[6] = 1.4
    b[7] = 1.6
    b[8] = 1.8
    b[9] = 2.0
    ye = calculate(b)
    print(ye)

    A = lagA(10)
    res = (1 / 0.2**4) * A * ye
    print(res)
