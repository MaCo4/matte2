from math import cos, tan


def sec(x):
    return 1 / cos(x)


if __name__ == "__main__":
    print("{:30}{:30}{}".format("x", "With loss of precision", "Without loss of precision"))

    for i in range(-1, -15, -1):
        x = 10 ** i
        loss = (1 - sec(x)) / (tan(x) ** 2)
        no_loss = -1 / (1 + sec(x))
        
        print("{:<30.16f}{:< 30.16f}{:< .16f}".format(x, loss, no_loss))
