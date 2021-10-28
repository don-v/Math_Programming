import numpy as np
from numpy import linalg
from chapter7_funcs import *

A31 = mat_maker((2,2), 2,-4,1,3)
A31aug = augmented_matrix_maker(A31)


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


inverse_solver(A31aug)
