from math import sqrt


if __name__ == "__main__":
    longleg = 3344556600
    shortleg = 1.2222222
    diff = shortleg ** 2 / (sqrt(longleg ** 2 + shortleg ** 2) + longleg)
    print("Difference between hypotenuse and the longest leg: {}".format(diff))
