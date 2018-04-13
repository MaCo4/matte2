from numpy.linalg import norm
from oppgave3 import y_approx_vector
from oppgave4c import y_exact_vector


if __name__ == "__main__":
    y_c = y_approx_vector()
    y_e = y_exact_vector()
    foroverfeil = norm(y_c - y_e, ord=1)

    print("foroverfeil:", foroverfeil)
