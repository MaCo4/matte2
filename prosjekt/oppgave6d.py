import scipy as sp
import math as m
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve, inv, norm
import matplotlib.pyplot as plt


def lagA(n):
    e = sp.ones(n)
    A = spdiags([e, -4.0 * e, 6.0 * e, -4.0 * e, e], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    B = csr_matrix([[16.0, -9.0, (8 / 3), (-1 / 4)],
                    [(16 / 17), (-60 / 17), (72 / 17), (-28 / 17)],
                    [(-12 / 17), (96 / 17), (-156 / 17), (72 / 17)]])

    A[0, 0: 4] = B[0, :]
    A[n - 2, n - 4: n] = B[1, :]
    A[n - 1, n - 4: n] = B[2, :]
    return A


def solve(A, b):
    y = spsolve(A, b)
    s = y.shape
    f = y[s[0] - 1]
    return f


E = 1.3 * 10 ** 10  # N/m^2
I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12
# f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
fx = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m
p = 100  # kg/m
L = 2.0
x = L

# eksakt løsning
y2halv = ((fx / (24 * E * I)) * (x ** 2) * ((x ** 2) - (4 * L * x) + (6 * (L ** 2))))
y2halv2 = (((9.81 * p * L) / (E * I * m.pi)) * (
(L ** 3 / m.pi ** 3) * 0 - (x ** 3 / 6) + ((L * x ** 2) / 2) - ((2 * L ** 2) / m.pi ** 2)))
bibkj = m.sin(m.pi * x / L)
y2 = y2halv - y2halv2
print("y2: ", y2)

B = [0.0] * 8
teoretiskfeil = [0.0] * 8
kondisjons = [0.0] * 8
emach = 2 ** (-52)
ntab = [0.0] * 8

for i in range(1, len(B) + 1):
    n = 10 * 2 ** i
    ntab[i - 1] = m.log(n)
    h = L / n  # h = L/n, der L = 2.0 meter
    b = [0.0] * n
    for j in range(0, n):
        sx = -100 * 9.81 * m.sin(m.pi / 2 * (h * j))
        b[j] = (h ** 4 / (E * I)) * (fx + sx)

    A = lagA(n)

    # feilen = eksakt - utregnet
    B[i - 1] = abs(abs(y2) - abs(solve(A, b)))

    AI = inv(A)
    k1 = norm(A, m.inf)
    k2 = norm(AI, m.inf)
    # print("kondisjonstall : ", k1*k2)
    print(k1, k2)

    kondisjons[i - 1] = abs(((k1 * k2) * emach))
    teoretiskfeil[i - 1] = abs((L ** 2) / (n ** 2))
    print("beregnet feil: ", kondisjons[i - 1])

# plt.plot(y2, solve(A, b))
feilen = plt.plot(ntab, B)
kondisjon = plt.plot(ntab, kondisjons)
teoretisk = plt.plot(ntab, teoretiskfeil)
plt.setp(feilen, color='r', label="oppg c")
plt.setp(kondisjon, color='b', label="kondisjon")
plt.setp(teoretisk, color='g', label="h^2")
plt.annotate('r = feil fra oppg c\nb = kondisjonstall\ng = teoretisk feil(h^2)', xy=(0.0, 0.030), xytext=(0.0, 0.03))
plt.ylabel("feil")
plt.xlabel("i-verdi")
plt.show()
