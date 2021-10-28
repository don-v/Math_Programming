import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def q_plus_kp(k,p,q, m):
    print(f'matrix before {k}*row{p} + row{q}:\n', m)
    m[q-1,:] = k*m[p-1,:] + m[q-1,:]
    print(f'matrix after {k}*row{p} + row{q}:\n', m, '\n')
    return m
    
def kq(k,q,m):
    print(f'matrix before {k}*row{q}:\n', m)
    m[q-1,:] = k*m[q-1,:]
    print(f'matrix after {k}*row{q}:\n', m, '\n')
    return m

def pqexchange(p,q,m):
    print(f'matrix before row exchange between {p} and {q}:\n', m)
    tmp = m[p-1,:].copy()
    # print('tmp:',tmp)
    # print('type of tmp:', type(tmp))
    m[p-1,:] = m[q-1,:]
    # print('row p before assign tmp to row q:', m[p-1,:])
    # print('row q before assign tmp to row q:', m[q-1,:])
    m[q-1,:] = tmp
    # print('row q after assign tmp to row q:', m[q-1,:])
    print(f'matrix after row exchange between {p} and {q}:\n', m)
    return m

def to_echelon(sq_mat):
    for j in range(sq_mat.shape[1]-1):
        for i in range(j,sq_mat.shape[0]):
            if i>j:
                mult = -1*(sq_mat[i,j]/sq_mat[j,j])
                q_plus_kp(mult,j+1,i+1,sq_mat)
    print(sq_mat)
    return sq_mat   

def echelon_solver(utmat):
    b = utmat[:,-1].copy()
    A = utmat[:,0:-1].copy()
    x = np.ones_like(b)
    for i in range((A.shape[0]-1),-1,-1):
        if i == A.shape[0]-1:
            x[i] = b[i]/A[i,i]
        else:
            Asub = A[i,i+1:].copy()
            xsub = x[i+1:].copy()
            outer = np.dot(Asub,xsub)
            x[i] = (b[i]-outer)/A[i,i]
    print('\nsolution x:\n', x)
    Abx = (A, x, b)
    print('A:\n', Abx[0])
    print(f'Ax:\n {Abx[0] @ Abx[1]} \nb:\n {Abx[2]}')
    return Abx
