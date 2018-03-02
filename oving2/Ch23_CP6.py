from numpy import matrix
from Ch21_CP1 import gaussian_elim_solve

if __name__ == "__main__":
    a = matrix([[10 ** (-20), 1],
                [          1, 2]])
    b = matrix([[1],
                [4]])

    x = gaussian_elim_solve(a, b)
    print("Eksempel 2:\nA=\n", a)
    print("\nx=\n", x)



    a = matrix([[          1, 2],
                [10 ** (-20), 1]])
    b = matrix([[4],
                [1]])

    x = gaussian_elim_solve(a, b)
    print("\n\nEksempel 3 med rader byttet:\nA=\n", a)
    print("\nx=\n", x)
