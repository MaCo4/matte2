from math import inf, log, sin


def fixed_point_iteration(func, initialGuess):
    x = initialGuess
    tolerance = 0.000000009
    prev_value = inf
    n = 0

    while n < 100000:  # Avoid infinite loop
        x = func(x)
        if abs(x - prev_value) < tolerance:
            break

        prev_value = x
        n += 1

    return x


def func_a(x):
    return (2*x + 2)**(1/3)


def func_b(x):
    return log(7 - x)


def func_c(x):
    return log(4 - sin(x))


if __name__ == "__main__":
    print("Exercise a: {:.8f}".format(fixed_point_iteration(func_a, 2)))
    print("Exercise b: {:.8f}".format(fixed_point_iteration(func_b, 2)))
    print("Exercise c: {:.8f}".format(fixed_point_iteration(func_c, 2)))
