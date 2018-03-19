from math import inf

from scipy.sparse.linalg import inv, norm

from Oppgave2 import lagA

if __name__ == "__main__":
    A = lagA(10)
    h = 0.2
    Ai = inv(A)
    cond = norm(A, ord=inf) * norm(Ai, ord=inf)
    print("cond(A)={}".format(cond))
    print(A.todense())

    A = (1 / h**4) * A
    Ai = inv(A)
    cond = norm(A, ord=inf) * norm(Ai, ord=inf)
    print("cond(1/h^4 * A)={}".format(cond))
    print(A.todense())
