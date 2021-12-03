from math import *
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt

MAX_ITER = 100

def f(x):
    return sin(x ** cos(x))

def der(f, x, eps):
    return (f(x + eps) - f(x)) / eps

def grad(x0, alpha, eps, f):
    x = [x0]
    i = 0
    while i < MAX_ITER:
        i += 1
        xNew = x[-1] - alpha * der(f, x[-1], 1e-6)
        x.append(xNew)
        if abs(x[-1] - x[-2]) < eps:
            break
    return x[:-1], x[-1]
f_v = np.vectorize(f)

x = np.arange(5., 6., 0.025)
y = f_v(x)

g_points, g_res = grad(5.1, 0.09, 0.0001, f)

print(g_points)
print(g_res)

print(f'{derivative(f, 5, dx=1e-6)} | {der(f, 5, 1e-6)} | {abs(derivative(f, 5, dx=1e-6) - der(f, 5, 1e-6))}')

plt.plot(x, y, label='function')
plt.scatter(g_points, f_v(g_points),  label='steps')
plt.scatter([g_res], [f(g_res)], marker='x', c='black',  label='result')
plt.legend(loc="upper right")
plt.show()