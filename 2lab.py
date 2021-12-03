from mynumpy import matrixMultMatrix, matrixMultVector, vectorMultVector
import numpy as np
import time
import random

def genVector(n):
    cRow = []
    for j in range(n):
        cRow.append(random.randrange(0, 11))
    return cRow

def genMatrix(m, n):
    C = []
    for i in range(m):
        C.append(genVector(n))
    return C

def trackTimeForFunc(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

m = 100
n = 150
k = 200

A = genMatrix(m, n)
B = genMatrix(n, k)

print(f"\nMatrix({m} x {n}) X Matrix({n} x {k})")
print(f"my {trackTimeForFunc(lambda: matrixMultMatrix(A, B))}")
print(f"np  {trackTimeForFunc(lambda: np.matmul(np.array(A), np.array(B)))}")

n = 1000

A = genMatrix(m, n)
B = genVector(n)

print(f"\nMatrix({m} x {n}) X Vector({n})")
print(f"my {trackTimeForFunc(lambda: matrixMultVector(A, B))}")
print(f"np  {trackTimeForFunc(lambda: (np.array(A)).dot(np.array(B)))}")

n = 10000

A = genVector(n)
B = genVector(n)

print(f"\nVector({n}) X Vector({n})")
print(f"my {trackTimeForFunc(lambda: vectorMultVector(A, B))}")
print(f"np  {trackTimeForFunc(lambda: np.multiply(np.array(A), np.array(B)))}")