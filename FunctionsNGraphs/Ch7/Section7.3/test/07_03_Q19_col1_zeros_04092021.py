import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from elim_04102021 import *

np.set_printoptions(precision=1, suppress=True)

""" what do we want our function to do?

takes a square matrix, and basically converts
all of the elements in the first column below
row 1 to zeros by doing row exchanges, adding
multiples of rows (kp+q), or by multiplying rows by
constant (kq)

and of course we should only be able to do so if
the element in the first column is not already zero,
and if the element above is non-zero.

so we have to check if the 1st element in the first 
row is not zero, if it is zero, we have to see if the
1st element for any of the other rows is non-zero, in
which case we can do a row-exchange and then carry on
with elimination. 



 """

t = np.arange(1,10).reshape(3,3)
# x = t.any()==0
# print(x)

y = t[1:,0]
b = t[:,-1]
uech = t[:,0:-1]

print('t:', t)
print('y:', y)
print('b:', b)
print('uech:',uech)

for y in range(5-1,-1,-1):
    print(y)

# for z in range(5,0):
#     print(z)
   
# x = dir(y)
# print(x)

# for row in t[1:,0]:
#     print(row)

# pqexchange(1,2,t)

# def q_plus_kp(k,p,q, m):
#     print(f'matrix before {k}*row{p} + row{q}:\n', m)
#     m[q-1,:] = k*m[p-1,:] + m[q-1,:]
#     print(f'matrix after {k}*row{p} + row{q}:\n', m, '\n')
#     return m
    
# def kq(k,q,m):
#     print(f'matrix before {k}*row{q}:\n', m)
#     m[q-1,:] = k*m[q-1,:]
#     print(f'matrix after {k}*row{q}:\n', m, '\n')
#     return m

# def pqexchange(p,q,m):


def col1_zeroes(sq_mat):
    for i in range(sq_mat.shape[0]):
        if i>0:
            mult = -1*(sq_mat[i,0]/sq_mat[0,0])
            q_plus_kp(mult,1,i+1,sq_mat)
    print(sq_mat)
    return sq_mat   

# col1_zeroes(t)

mat = np.array(
    [
    [2, -1, -2, 2, -5, 2],
    [1, 3, -2, 1, -2, -5],
    [-1, 4, 2, -3, 8, -4],
    [3, -2, -4, 1, -3, -3],
    [4, -6, 1, -2, 1, 10]
    ]
    ).astype(float)

# col1_zeroes(mat)

# sub_mat = mat[1:,1:]
# print('sub:\n', sub_mat)

# print('full:\n', mat[0:,0:])

# for j in range(mat.shape[1]-1):
#     for i in range(mat.shape[0]):
#         print(i,j)

def col1_zeroes2(sq_mat):
    for j in range(sq_mat.shape[1]-1):
        for i in range(j,sq_mat.shape[0]):
            if i>j:
                mult = -1*(sq_mat[i,j]/sq_mat[j,j])
                q_plus_kp(mult,j+1,i+1,sq_mat)
    print(sq_mat)
    return sq_mat   

# col1_zeroes2(mat)


def solve_upperT(utmat):
    x5 = utmat[4,5]/utmat[4,4]
    x4 = (utmat[3,5] - (utmat[3,4]*x5))/utmat[3,3]
    x3 = (utmat[2,5] - ((utmat[2,4]*x5) + (utmat[2,3]*x4)))/utmat[2,2]
    x2 = (utmat[1,5] - ((utmat[1,4]*x5) + (utmat[1,3]*x4) + (utmat[1,2]*x3)))/utmat[1,1]
    x1 = (utmat[0,5] - ((utmat[0,4]*x5) + (utmat[0,3]*x4) + (utmat[0,2]*x3) + (utmat[0,1]*x2)))/utmat[0,0]
    sol = [x1, x2, x3, x4, x5]
    return [int(y) for y in sol]

# print(solve_upperT(col1_zeroes2(mat)))

uech2 = col1_zeroes2(mat)

def solve_upperT2(utmat):
    b = utmat[:,-1].copy()
    A = utmat[:,0:-1].copy()
    # x = np.empty(shape=A.shape[1],dtype=np.int8)
    x = np.ones_like(b)
    # print('b:\n', b)
    # print('A:\n', A)
    for i in range((A.shape[0]-1),-1,-1):
        if i == A.shape[0]-1:
            x[i] = b[i]/A[i,i]
            # print('x:', x)  
            # return x              
        else:
            Asub = A[i,i+1:].copy()
            xsub = x[i+1:].copy()
            outer = np.dot(Asub,xsub)
            # print('Asub:\n', Asub, '\nxsub:\n', xsub, '\nOuter:\n', outer)
            # print('\n')
            x[i] = (b[i]-outer)/A[i,i]
            # print('i:\n', i, '\nx:\n', x)   
    print('\nsolution:\n', x)
    return x
    
            


solve_upperT2(uech2)

# solve_upperT2(col1_zeroes2(mat))




