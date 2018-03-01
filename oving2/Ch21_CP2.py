from numpy.ma import ones
from scipy.linalg import hilbert
from Ch21_CP1 import gaussian_elim_solve


def solve_hilbert(n):
    H = hilbert(n)
    b = ones((n, 1))
    return gaussian_elim_solve(H, b)


if __name__ == "__main__":
    print("Oppgave a: n=2")
    print("x =")
    print(solve_hilbert(2))

    print("\nOppgave b: n=5")
    print("x =")
    print(solve_hilbert(5))

    print("\nOppgave c: n=10")
    print("x =")
    print(solve_hilbert(10))
