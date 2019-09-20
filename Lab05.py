#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import sympy as sp

A = np.array([[1,2,0],
             [1,0,1],
             [0,1,0]])
B = np.array([[2,0,1],
             [1,1,-4],
             [3,7,-3]])
C = np.array([[1,1,0],
             [1,0,1],
             [0,1,0],
             [1,2,3]])

def Aumentar(a):
    Valor = 'h' + str(sp.Matrix(a).shape)
    Identidad = sp.eye(int(Valor[2]))
    for x in range(0, int(Valor[2])):
        Identidad = Identidad.col_insert(x, sp.Matrix(a).col(x))
    return Identidad

invA1 = np.linalg.inv(A)
invA2 = sp.Matrix(A).inv()
invA3 = Aumentar(A).rref()
print("inversa con numpy:\n {} \n inversa con sympy:\n {} \n inversa con FERR:\n {} \n".format(invA1, invA2, invA3))

invB1 = np.linalg.inv(B)
invB2 = sp.Matrix(B).inv()
invB3 = Aumentar(B).rref()
print("inversa con numpy:\n {} \n inversa con sympy:\n {} \n inversa con FERR:\n {} \n".format(invB1, invB2, invB3))

print("C no tiene inversa \n")

RangoA = np.linalg.matrix_rank(A)
RangoB = np.linalg.matrix_rank(B)
RangoC = np.linalg.matrix_rank(C)
NumcolsA = A.shape[1]
NumcolsB = B.shape[1]
NumcolsC = C.shape[1]
NulidadA = RangoA - NumcolsA
NulidadB = RangoB - NumcolsB
NulidadC = RangoC - NumcolsC
NullSpaceA = str(sp.Matrix(A).nullspace())
NullSpaceB = sp.Matrix(B).nullspace()
NullSpaceC = sp.Matrix(C).nullspace()

print(" Rango de A: {} \n Rango de B: {} \n Rango de C: {} \n".format(RangoA, RangoB, RangoC))
print(" Nulidad A: {} \n Nulidad B: {} \n Nulidad C: {} \n ".format(NulidadA, NulidadB, NulidadC))
print(" Espacio nulo de A:\n {} \n Espacio nulo de B:\n {} \n Espacio nulo de C:\n {} \n".format(NullSpaceA, NullSpaceB, NullSpaceC))

