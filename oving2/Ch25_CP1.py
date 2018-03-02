from numpy import ones, zeros, dot, reshape, diag, amax, absolute
from scipy.sparse import dia_matrix, coo_matrix


"""
Koden er hentet fra python-oversettelser av MATLAB-koder fra boka, med små modifikasjoner.
Hentet fra http://blue.math.buffalo.edu/sauer2py/sparsesetup.py
"""
def sparsesetup(n):
    e = ones(n)
    n2 = n / 2
    a = dia_matrix(([-e, 3 * e, -e], [-1, 0, 1]), shape=(n, n)).tocsr()
    c = coo_matrix((e / 2, (range(n), range(n - 1, -1, -1))), shape=(n, n)).tocsr()
    a = a + c
    a[n2, n2 - 1] = -1
    a[n2 - 1, n2] = -1
    b = zeros(n)
    b[0] = 2.5
    b[-1] = 2.5
    b[1:n - 1] = 1.5
    b[int(n2 - 1):int(n2 + 1)] = 1.0
    return a, b


"""
Koden er hentet fra python-oversettelser av MATLAB-koder fra boka, med små modifikasjoner.
Hentet fra http://blue.math.buffalo.edu/sauer2py/jacobi.py
"""
def jacobi(a, b, k):
    n = len(b)
    d = [a[i, i] for i in range(n)]
    r = a - diag(d)
    x = zeros((n, 1))
    bb = reshape(b, (n, 1))
    dd = reshape(d, (n, 1))

    xcorrect = ones(n)
    tolerance = 0.000001
    while True and k > 0:  # Hold på i maks k steg
        x = (bb - dot(r, x)) / dd

        if amax(absolute(x - xcorrect)) < tolerance:
            break
        k -= 1

    return x


if __name__ == "__main__":
    n = 100
    a, _ = sparsesetup(n)
    b = ones(n)
    b[0] = 2
    b[n-1] = 2  # b = [2, 1, 1, ..., 1, 1, 2]
    print(jacobi(a, b, 10000))
