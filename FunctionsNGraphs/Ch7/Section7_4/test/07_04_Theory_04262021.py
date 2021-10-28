# print(__name__)
# import numpy as np
from numpy import linalg
from chapter7_funcs_src import *

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
#     print(f'matrix before row exchange between {p} and {q}:\n', m)
#     tmp = m[p-1,:].copy()
#     # print('tmp:',tmp)
#     # print('type of tmp:', type(tmp))
#     m[p-1,:] = m[q-1,:]
#     # print('row p before assign tmp to row q:', m[p-1,:])
#     # print('row q before assign tmp to row q:', m[q-1,:])
#     m[q-1,:] = tmp
#     # print('row q after assign tmp to row q:', m[q-1,:])
#     print(f'matrix after row exchange between {p} and {q}:\n', m)
#     return m

# def to_echelon(sq_mat):
#     for j in range(sq_mat.shape[1]-1):
#         for i in range(j,sq_mat.shape[0]):
#             if i>j:
#                 mult = -1*(sq_mat[i,j]/sq_mat[j,j])
#                 q_plus_kp(mult,j+1,i+1,sq_mat)
#     print(sq_mat)
#     return sq_mat   

# def echelon_solver(utmat):
#     b = utmat[:,-1].copy()
#     A = utmat[:,0:-1].copy()
#     x = np.ones_like(b)
#     for i in range((A.shape[0]-1),-1,-1):
#         if i == A.shape[0]-1:
#             x[i] = b[i]/A[i,i]
#         else:
#             Asub = A[i,i+1:].copy()
#             xsub = x[i+1:].copy()
#             outer = np.dot(Asub,xsub)
#             x[i] = (b[i]-outer)/A[i,i]
#     print('\nsolution x:\n', x)
#     Abx = (A, x, b)
#     print('A:\n', Abx[0])
#     print(f'Ax:\n {Abx[0] @ Abx[1]} \nb:\n {Abx[2]}')
#     return Abx

# def mat_maker(shape, *args):
#     x = []
#     for arg in args:
#         x.append(arg)
#     mat = np.array(x)
#     mat.resize(shape)
#     return mat 

# def ex1_8(A, B):
#     print('A:\n', A)
#     print('B:\n', B)
#     print('A+B:\n', f'{A+B}')
#     print('A-B:\n', f'{A-B}')
#     print('2A:\n', f'{2*A}')
#     print('-3B:\n', f'{-3*B}')

# def ex9_18(A,B):
#     print('A:\n', A)
#     print('B:\n', B)
#     print('AB:\n', f'{A@B}')
#     print('BA:\n', f'{B@A}')
    
# def ex19_22(A,B):
#     print('A:\n', A)
#     print('B:\n', B)
#     print('AB:\n', f'{A@B}')

# def ex23(A,B):
#     print('\nQ23:')
#     print('A:\n', A)
#     print('B:\n', B)
#     print('(A+B)*(A-B):\n', f'{(A+B)@(A-B)}')
#     print('A^2-B^2:\n', f'{(A@A)-(B@B)}')

# def ex24(A,B):
#     print('\nQ24:')
#     print('A:\n', A)
#     print('B:\n', B)
#     print('(A+B)*(A+B):\n', f'{(A+B)@(A+B)}')
#     print('A^2+2AB+B^2:\n', f'{(A@A)+(2*(A@B))+(B@B)}')

# def ex25(A,B,C):
#     print('\nQ25:')
#     print('A:\n', A)
#     print('B:\n', B)
#     print('C:\n', C)
#     print('A*(B+C):\n', f'{A@(B+C)}')
#     print('AB+AC:\n', f'{(A@B)+(A@C)}')

# def ex26(A,B,C):
#     print('\nQ26:')
#     print('A:\n', A)
#     print('B:\n', B)
#     print('C:\n', C)
#     print('A(BC):\n', f'{A@(B@C)}')
#     print('(AB)C:\n', f'{(A@B)@C}')

# def augmented_matrix_maker(A):
#     A_identity = np.identity(A.shape[0])
#     aug = np.concatenate((A,A_identity),axis=1)
#     print('A:\n', A)
#     print('Augmented Matrix:\n', aug)
#     return aug

# def inverse_solver(aug_mat):
#     for j in range(aug_mat.shape[0]-1):
#         for i in range(j,aug_mat.shape[0]):
#             if i>j:
#                 mult = -1*(aug_mat[i,j]/aug_mat[j,j])
#                 q_plus_kp(mult,j+1,i+1,aug_mat)
    
#     for k in range(aug_mat.shape[0]-1,-1,-1):
#         for l in range(k,-1,-1):
#             if l<k:
#                 mult = -1*(aug_mat[l,k]/aug_mat[k,k])
#                 q_plus_kp(mult,k+1,l+1,aug_mat)

#     for m in range(aug_mat.shape[0]):
#         for n in range(aug_mat.shape[0]):
#             if m == n:
#                 if aug_mat[m,n] == 1:
#                     continue
#                 else:
#                     c = 1/(aug_mat[m,n])
#                     kq(c,m+1,aug_mat)

#     inv = aug_mat[:,-aug_mat.shape[0]:]
#     print('aug_mat:\n', aug_mat)
#     print('inv:\n',inv)
#     return inv

# A1 = mat_maker((2,2), 5, -2, 1, 3)
# B1 = mat_maker((2,2), 4, 1, -3, 2)

# ex1_8(A1, B1)

# A2 = mat_maker((2,2), 3, 0, -1, 2)
# B2 = mat_maker((2,2), 3, -4, 1, 1)

# ex1_8(A2, B2)

# A3 = mat_maker((3,2), 6, -1, 2, 0, -3, 4)
# B3 = mat_maker((3,2), 3, 1, -1, 5, 6, 0)

# ex1_8(A3, B3)

# A4 = mat_maker((2,3), 0,-2,7,5,4,-3)
# B4 = mat_maker((2,3), 8,4,0,0,1,4)

# ex1_8(A4, B4)

# A5 = mat_maker((1,3), 4,-3,2)
# B5 = mat_maker((1,3), 7,0,-5)

# ex1_8(A5, B5)

# A6 = mat_maker((2,1), 7,-16)
# B6 = mat_maker((2,1), -11,9)

# ex1_8(A6, B6)

# A7 = mat_maker((2,4), 0,4,0,3,1,2,0,-5)
# B7 = mat_maker((2,4), -3,0,1,3,2,0,7,-2)

# ex1_8(A7, B7)

# A8 = mat_maker((1,1), -7)
# B8 = mat_maker((1,1), 9)

# ex1_8(A8, B8)


# A9 = mat_maker((2,2), 2,6,3,-4)
# B9 = mat_maker((2,2), 5,-2,1,7)

# ex9_18(A9, B9)

# A10 = mat_maker((2,2), 4,-2,-2,1)
# B10 = mat_maker((2,2), 2,1,4,2)

# ex9_18(A10, B10)

# A11 = mat_maker((3,3), 3,0,-1,0,4,2,5,-3,1)
# B11 = mat_maker((3,3), 1,-5,0,4,1,-2,0,-1,3)

# ex9_18(A11, B11)

# A12 = mat_maker((3,3), 5,0,0,0,-3,0,0,0,2)
# B12 = mat_maker((3,3), 3,0,0,0,4,0,0,0,-2)

# ex9_18(A12, B12)

# A13 = mat_maker((2,3), 4,-3,1,-5,2,2)
# B13 = mat_maker((3,2), 2,1,0,1,-4,7)

# ex9_18(A13, B13)

# A14 = mat_maker((3,4), 2,1,-1,0, 3,-2,0,5, -2,1,4,2)
# B14 = mat_maker((4,3), 5,-3,1, 1,2,0, -1,0,4, 0,-2,3)

# ex9_18(A14, B14)

# A15 = mat_maker((3,3), 1,2,3,4,5,6,7,8,9)
# B15 = mat_maker((3,3), 1,0,0, 0,1,0, 0,0,1)

# ex9_18(A15, B15)

# A16 = mat_maker((3,3), 1,2,3,2,3,1,3,1,2)
# B16 = mat_maker((3,3), 2,0,0, 0,2,0, 0,0,2)

# ex9_18(A16, B16)

# A17 = mat_maker((1,3), -3,7,2)
# B17 = mat_maker((3,1), 1,4,-5)

# ex9_18(A17, B17)

# A18 = mat_maker((1,2), 4,8)
# B18 = mat_maker((2,1), -3,2)

# ex9_18(A18, B18)

# A19 = mat_maker((3,2), 4,-2, 0,3, -7,5)
# B19 = mat_maker((2,1), 3,4)

# ex19_22(A19, B19)

# A20 = mat_maker((3,1), 4,-3,2)
# B20 = mat_maker((1,2), 5,1)

# ex19_22(A20, B20)

# A21 = mat_maker((2,4), 2,1,0,-3, -7,0,-2,4)
# B21 = mat_maker((4,3), 4,-2,0, 1,1,-2, 0,0,5, -3,-1,0)

# ex19_22(A21, B21)

# A22 = mat_maker((2,3), 1,2,-3, 4,-5,6)
# B22 = mat_maker((3,4), 1,-1,0,2, -2,3,1,0, 0,4,0,-3)

# ex19_22(A22, B22)

# A22 = mat_maker((2,3), 1,2,-3, 4,-5,6)
# B22 = mat_maker((3,4), 1,-1,0,2, -2,3,1,0, 0,4,0,-3)

# ex19_22(A22, B22)

# A23 = mat_maker((2,2), 1,2,0,-3)
# B23 = mat_maker((2,2), 2,-1,3,1)

# ex23(A23,B23)
# ex24(A23,B23)

# C25 = mat_maker((2,2), 3,1,-2,0)

# ex25(A23,B23,C25)
# ex26(A23,B23,C25)

# A31 = mat_maker((2,2), 2,-4,1,3)
# A31aug = augmented_matrix_maker(A31)
# q_plus_kp((-1/2), 1,2,A31aug)
# q_plus_kp((4/5),2,1,A31aug)
# kq((1/2),1,A31aug)
# kq((1/5),2,A31aug)

# print('elim aug:\n', A31aug[:,-2:])
# print('linalg inv:\n', linalg.inv(A31))

# A32 = mat_maker((2,2), 3,2,4,5)
# A32aug = augmented_matrix_maker(A32)

#     print(aug_mat)
#     return aug_mat 

# A31 = mat_maker((2,2), 2,-4,1,3)
# A31aug = augmented_matrix_maker(A31)

# inverse_solver(A31aug)

# A32 = mat_maker((2,2), 3,2,4,5)
# A32aug = augmented_matrix_maker(A32)
# A32inv = inverse_solver(A32aug)
# print(f'A32@A32^-1:\n{A32@A32inv}')

# A33 = mat_maker((2,2), 2,4,4,8)
# A33aug = augmented_matrix_maker(A33)
# A33inv = inverse_solver(A33aug)
# print(f'A33@A33^-1:\n{A33@A33inv}')

# A34 = mat_maker((2,2), 2,4,4,8)
# A34aug = augmented_matrix_maker(A34)
# A34inv = inverse_solver(A34aug)
# print(f'A34@A34^-1:\n{A34@A34inv}')

# A35 = mat_maker((3,3), 3,-1,0, 2,2,0, 0,0,4)
# A35aug = augmented_matrix_maker(A35)
# A35inv = inverse_solver(A35aug)
# print(f'A35@A35^-1:\n{A35@A35inv}')
