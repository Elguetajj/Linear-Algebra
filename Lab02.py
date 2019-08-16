#!/usr/bin/env python
# coding: utf-8

# In[241]:


Num1= 8
Num2= 4
print(f"Num1:{Num1}")
print(f"Num2:{Num2}")

Arr=[Num1-Num2,Num1+Num2,Num1*Num2,Num1/Num2]
Ops=["Substraction","Addition","Multiplication","Division"]

for operation, result in zip(Ops, Arr):
    print('the {} of {} and {} is {}'.format(operation, Num1, Num2, result))

Arr2=[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]


def printarr(arr):
    for row in arr:
        for val in row:
            print (f"{val}", end=',')
        print()

print()
printarr(Arr2)

def changediagonal(arr):
    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if i==j:
                arr[i][j]=0
            
            
print()
changediagonal(Arr2)        
printarr(Arr2)


# In[ ]:




