import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import tridiagonal
from problimite import problimite

a = 0
b = 10

alpha = 0
beta = 0

def Q_func(x):
    return 0

def R_func(x):
    return 1

def solution_exacte(x):
    return (x * (10 - x)) / 2

h1 = 2
N1 = int((b - a) / h1 - 1)

x1 = np.linspace(a + h1, b - h1, N1)
Q1 = [Q_func(xi) for xi in x1]
R1 = [R_func(xi) for xi in x1]

y1 = problimite(N1, Q1, R1, a, b, alpha, beta)
x_plot1 = np.linspace(a, b, N1 + 2)

h2 = 1
N2 = int((b - a) / h2 - 1)

x2 = np.linspace(a + h2, b - h2, N2)
Q2 = [Q_func(xi) for xi in x2]
R2 = [R_func(xi) for xi in x2]

y2 = problimite(N2, Q2, R2, a, b, alpha, beta)
x_plot2 = np.linspace(a, b, N2 + 2)

x_exact = np.linspace(a, b, 100)
y_exact = solution_exacte(x_exact)

plt.figure()

plt.plot(x_plot1, y1, 'o-', label='Approx h=2')
plt.plot(x_plot2, y2, 's-', label='Approx h=1')
plt.plot(x_exact, y_exact, '-', label='Solution exacte')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparaison des solutions')
plt.legend()
plt.grid()

plt.show()