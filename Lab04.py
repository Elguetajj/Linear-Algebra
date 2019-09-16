#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import sympy as sp
import plotly as plt
import matplotlib as mat

A = np.arange(15*15).reshape(15,15)
B = np.arange(15*15).reshape(15,15)
np.fill_diagonal(A,0)
np.fill_diagonal(B,1)

suma = A + B
resta = A - B
producto = A*B

AT = A.transpose()
BT = B.transpose()

C = np.array(np.random.rand(20))
D = np.array(np.random.rand(20))

CD = C * D

