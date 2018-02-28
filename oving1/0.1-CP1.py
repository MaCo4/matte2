from numpy.ma import zeros, ones


def nest(c, x, b=None):
    n = len(c) - 1
    if b is None:
        b = zeros(n)

    y = c[n]
    for i in range(n - 1, -1, -1):
        y *= (x - b[i])
        y += c[i]

    return y


if __name__ == "__main__":
    x = 1.00001
    nested = nest(ones(51), x)
    accurate = (x**51 - 1) / (x - 1)

    print("Nested: {}".format(nested))
    print("Accurate: {}".format(accurate))
    print("Diff: {}".format(nested - accurate))
