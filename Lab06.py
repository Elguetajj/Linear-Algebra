#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import sympy as sp
import time as tm

A = np.array([[1,1,0],
              [1,0,1],
              [0,1,0]])
B = np.array([[1,1,0,1],
              [1,0,1,0],
              [0,1,0,0],
              [0,1,0,0]])
b1 = np.array([[1],
              [2],
              [4]])
b2 = np.array([[1],
               [8],
               [4],
               [5]])

def CrammersRule(A,b):
    sol = []
    for i in range(len(b)):
        temp = A.copy()
        temp[:,i] = b[:,0]
        sol.append(round(np.linalg.det(temp)/np.linalg.det(A),1))
    return sol

InvA = np.linalg.inv(A)
InvASP = sp.Matrix(A).inv()
print(f"Inversa de A: \n {InvA}")
InvB = "no tiene inversa"
print(f"{InvB}")

DetA = np.linalg.det(A)
print(f"Determinante de A: {DetA}")
DetB = np.linalg.det(B)
print(f"Determinante de B: {DetB}\n")

print("Ax = b1")
SolInvNP = InvA.dot(b1)
print(f"Solucion con Inversa numpy: \n {SolInvNP}")

SolInvSP = InvASP*sp.Matrix(b1)
print(f"Solucion con inversa sympy: \n {SolInvSP}")

SolCrammer = CrammersRule(A, b1)
print(f"Solucion con Regla de Crammer:\n {SolCrammer} \n")

print("el sistema Bx = b2 no se puede solucionar con la inversa ni con crammer ya que su determinante es 0")



C = np.random.rand(100, 100)
d = np.random.rand(100, 1)
InvCNP = np.linalg.inv(C)
InvCSP = sp.Matrix(C).inv()

print("Cx = d")

start = tm.time()
SolInvNP = InvCNP.dot(d)
print(f"Solucion con Inversa numpy: \n {SolInvNP}")
print("Time: "+str(tm.time()-start)+"\n")

start = tm.time()
SolInvSP = InvCSP*sp.Matrix(d)
print(f"Solucion con inversa sympy: \n {SolInvSP}")
print("Time: "+str(tm.time()-start)+"\n")

start = tm.time()
SolCrammer = CrammersRule(C, d)
print(f"Solucion con Regla de Crammer:\n {SolCrammer}")
print("Time: "+str(tm.time()-start)+"\n")


D = np.random.rand(500, 500)
d2 = np.random.rand(500, 1)
InvCNP = np.linalg.inv(D)
InvCSP = sp.Matrix(D).inv()

print("Dx = d2")

start = tm.time()
SolInvNP = InvCNP.dot(d2)
print(f"Solucion con Inversa numpy: \n {SolInvNP}")
print("Time: "+str(tm.time()-start)+"\n")

start = tm.time()
SolInvSP = InvCSP*sp.Matrix(d2)
print(f"Solucion con inversa sympy: \n {SolInvSP}")
print("Time: "+str(tm.time()-start)+"\n")

start = tm.time()
SolCrammer = CrammersRule(D, d2)
print(f"Solucion con Regla de Crammer:\n {SolCrammer}")
print("Time: "+str(tm.time()-start)+"\n")


