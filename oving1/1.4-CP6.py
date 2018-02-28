from math import pi, inf


if __name__ == "__main__":
    r = 2  # Initial guess
    tolerance = 0.00009
    prev_value = inf
    n = 0

    func = lambda x: (2 * x ** 3 + 10 * x ** 2 - 180 / pi)
    deriv = lambda x: (6 * x ** 2 + 20 * x)

    while n < 100000:  # Avoid infinite loop
        r = r - func(r) / deriv(r)

        if abs(r - prev_value) < tolerance:
            break

        prev_value = r
        n += 1

    print("Radius = {:.4f}".format(r))
