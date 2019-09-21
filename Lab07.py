#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import sympy as sp
import time as tm

A = np.array([[1,1,0],
              [1,0,1],
              [0,1,0]])
B = np.array([[2,0,1,1],
              [1,1,2,0],
              [3,7,-3,1],
              [1,2,0,1]])
C = np.array([[1,1,0,1],
              [1,0,1,0],
              [0,1,0,0],
              [0,1,0,0]])
EigANP = np.linalg.eigvals(A)
print(f"Eigenvalores de A con numpy: \n {EigANP} \n")
EigASP = sp.Matrix(A).eigenvals()
print(f"Eigenvalores de A con sympy: \n {EigASP} \n")

start = tm.time()
EigVANP = np.linalg.eig(A)
print(f"Eigenvectores de A con numpy: \n {EigVANP} \n")
print("Time: "+str(tm.time()-start)+"\n")

start = tm.time()
EigVASP = sp.Matrix(A).eigenvects()
print(f"Eigenvectores de A con sympy: \n {EigVASP} \n")
print("Time: "+str(tm.time()-start)+"\n")


EigBNP = np.linalg.eigvals(B)
print(f"Eigenvalores de B con numpy: \n {EigBNP} \n")
EigBSP = sp.Matrix(B).eigenvals()
print(f"Eigenvalores de B con sympy: \n {EigBSP} \n")
EigVBNP = np.linalg.eig(B)
print(f"Eigenvectores de B con numpy: \n {EigVBNP} \n")
EigVBSP = sp.Matrix(B).eigenvects()
print(f"Eigenvectores de B con sympy: \n {EigVBSP} \n")


EigCNP = np.linalg.eigvals(C)
print(f"Eigenvalores de C con numpy: \n {EigCNP} \n")
EigCSP = sp.Matrix(C).eigenvals()
print(f"Eigenvalores de C con sympy: \n {EigCSP} \n")
EigVCNP = np.linalg.eig(C)
print(f"Eigenvectores de C con numpy: \n {EigVCNP} \n")
EigVCSP = sp.Matrix(C).eigenvects()
print(f"Eigenvectores de C con sympy: \n {EigVCSP} \n")

DiagA = sp.Matrix(A).diagonalize
print(f"Diagonalizacion de A con sympy: \n {DiagA} \n")
PolA = sp.Matrix(A).charpoly()
print(f"Polinomio caracteristico de A con sympy: \n {PolA} \n")

DiagC = sp.Matrix(C).diagonalize
print(f"Diagonalizacion de A con sympy: \n {DiagC} \n")
PolC = sp.Matrix(C).charpoly()
print(f"Polinomio caracteristico de A con sympy: \n {PolC} \n")

