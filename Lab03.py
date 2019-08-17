#!/usr/bin/env python
# coding: utf-8

# In[85]:


### import plotly.graph_objects as go
import numpy as np
import sympy as sp
from sympy import Symbol


X = Symbol('x')

def f1(x):
    return 2*x-10
def f2(x):
    return  6-x
def f3(x):
    return x+6

x= np.linspace(-20,20,100)
fig=go.Figure()
fig.add_trace(go.Scatter(x=n, y=f1(x), 
                        mode= 'lines',
                        name='f1(x)=2x-10'))
fig.add_trace(go.Scatter(x=n, y= f2(x), 
                        mode= 'lines',
                        name= 'f2(x)=6-x'))
fig.add_trace(go.Scatter(x=n, y= f3(x),
                        mode= 'lines',
                        name= 'f3(x)=x+6'))

x1, = sp.solve(f1(X)-f2(X),rational=None)
x2, = sp.solve(f1(X)-f3(X),rational=False)
x3, = sp.solve(f2(X)-f3(X),rational=False)

y1= f1(x1)
y2= f1(x2)
y3= f2(x3)

fig.add_trace(go.Scatter(x=[float(x1),float(x2),float(x3),float(x1)],y=[float(y1),float(y2),float(y3),float(y1)],
                         fill='toself',
                         fillcolor='rgb(184, 247, 212)',
                         mode= 'lines',
                         name= 'f3(x)=x+6'))


print (x1)
fig.show()


