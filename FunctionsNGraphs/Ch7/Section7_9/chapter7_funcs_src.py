# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


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

def echelon_solver2(utmat):
    b = utmat[:,-1].copy()
    A = utmat[:,0:-1].copy()
    x = np.ones_like(b).astype('float32')
    for i in range((A.shape[0]-1),-1,-1):
        if i == A.shape[0]-1:
            x[i] = b[i]/A[i,i]
            print(f"""
            A.shape[0]-1 = {A.shape[0]-1}
            i = {i}
            x[i] = {x[i]}        
            b[i] = {b[i]}
            A[i,i] = {A[i,i]}

            id(x) = {id(x)}
            id(b) = {id(b)}
            id(A) = {id(A)}
            """)
        else:
            Asub = A[i,i+1:].copy()
            xsub = x[i+1:].copy()
            outer = np.dot(Asub,xsub)
            x[i] = (b[i]-outer)/A[i,i]
            print(f"""
            A.shape[0]-1 = {A.shape[0]-1}
            i = {i}
            x[i] = {x[i]}        
            b[i] = {b[i]}
            Asub = {Asub}
            xsub = {xsub}
            """)
    print('\nsolution x:\n', x)
    Abx = (A, x, b)
    print('A:\n', Abx[0])
    print(f'Ax:\n {Abx[0] @ Abx[1]} \nb:\n {Abx[2]}')
    return Abx

# def mat_maker(shape, *args):
#     x = []
#     for arg in args:
#         x.append(arg)
#     mat = np.array(x)
#     mat.resize(shape)
#     return mat 

def mat_maker2(shape, *args):
    x = []
    for arg in args:
        x.append(arg)
    mat = np.array(x).astype('float32')
    mat.resize(shape)
    return mat 

def ex1_8(A, B):
    print('A:\n', A)
    print('B:\n', B)
    print('A+B:\n', f'{A+B}')
    print('A-B:\n', f'{A-B}')
    print('2A:\n', f'{2*A}')
    print('-3B:\n', f'{-3*B}')

def ex9_18(A,B):
    print('A:\n', A)
    print('B:\n', B)
    print('AB:\n', f'{A@B}')
    print('BA:\n', f'{B@A}')
    
def ex19_22(A,B):
    print('A:\n', A)
    print('B:\n', B)
    print('AB:\n', f'{A@B}')

def ex23(A,B):
    print('\nQ23:')
    print('A:\n', A)
    print('B:\n', B)
    print('(A+B)*(A-B):\n', f'{(A+B)@(A-B)}')
    print('A^2-B^2:\n', f'{(A@A)-(B@B)}')

def ex24(A,B):
    print('\nQ24:')
    print('A:\n', A)
    print('B:\n', B)
    print('(A+B)*(A+B):\n', f'{(A+B)@(A+B)}')
    print('A^2+2AB+B^2:\n', f'{(A@A)+(2*(A@B))+(B@B)}')

def ex25(A,B,C):
    print('\nQ25:')
    print('A:\n', A)
    print('B:\n', B)
    print('C:\n', C)
    print('A*(B+C):\n', f'{A@(B+C)}')
    print('AB+AC:\n', f'{(A@B)+(A@C)}')

def ex26(A,B,C):
    print('\nQ26:')
    print('A:\n', A)
    print('B:\n', B)
    print('C:\n', C)
    print('A(BC):\n', f'{A@(B@C)}')
    print('(AB)C:\n', f'{(A@B)@C}')

def augmented_matrix_maker(A):
    A_identity = np.identity(A.shape[0])
    aug = np.concatenate((A,A_identity),axis=1)
    print('A:\n', A)
    print('Augmented Matrix:\n', aug)
    return aug

def inverse_solver(aug_mat):
    for j in range(aug_mat.shape[0]-1):
        for i in range(j,aug_mat.shape[0]):
            if i>j:
                mult = -1*(aug_mat[i,j]/aug_mat[j,j])
                q_plus_kp(mult,j+1,i+1,aug_mat)
    
    for k in range(aug_mat.shape[0]-1,-1,-1):
        for l in range(k,-1,-1):
            if l<k:
                mult = -1*(aug_mat[l,k]/aug_mat[k,k])
                q_plus_kp(mult,k+1,l+1,aug_mat)

    for m in range(aug_mat.shape[0]):
        for n in range(aug_mat.shape[0]):
            if m == n:
                if aug_mat[m,n] == 1:
                    continue
                else:
                    c = 1/(aug_mat[m,n])
                    kq(c,m+1,aug_mat)

    inv = aug_mat[:,-aug_mat.shape[0]:]
    print('aug_mat:\n', aug_mat)
    print('inv:\n',inv)
    return inv