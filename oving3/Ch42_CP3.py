from numpy import matrix, ones
from numpy.linalg import solve
from math import log, exp


def exponential_model_linearize(x, y):
    A = matrix(ones((len(x), 2)))
    for i, x in enumerate(x):
        A[i, 1] = x

    b = matrix(ones((len(y), 1)))
    for i, y in enumerate(y):
        b[i, 0] = log(y)

    c = solve(A.T * A, A.T * b)

    return {"A": A, "b": b, "c": c}


if __name__ == "__main__":
    x = [1960, 1970, 1990, 2000]
    y = [3039585530, 3707475887, 5281653820, 6079603571]

    exp_model = exponential_model_linearize(x, y)
    exp_model_c = exp_model['c']
    c1 = exp(exp_model_c[0, 0])  # Siden k = ln c1, er c1 = e^k

    y_exp_model = lambda t: c1 * exp(exp_model_c[1, 0] * t)
    print("y_exp_model(1980) = {}".format(y_exp_model(1980)))
