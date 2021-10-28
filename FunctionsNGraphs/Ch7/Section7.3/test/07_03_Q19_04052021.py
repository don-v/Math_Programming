import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=1, suppress=True)

mat = np.array(
    [
    [2, -1, -2, 2, -5, 2],
    [1, 3, -2, 1, -2, -5],
    [-1, 4, 2, -3, 8, -4],
    [3, -2, -4, 1, -3, -3],
    [4, -6, 1, -2, 1, 10]
    ]
    ).astype(float)

# print(mat)
# r1r2 = -0.5*mat[0,:]
# print('\n', r1r2)
# r2 = mat[1,:]
# print('\n', r2)
# print('\n', r1r2 + r2)
# print('\n',mat)

# a = np.array([1, 2])
# b = np.array([2, 3])

# print('\n', a,'\n', b, '\n', a+b)

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



# q_plus_kp(-0.5, 1, 2, mat)
# q_plus_kp(0.5, 1, 3, mat)
# kq(2,2,mat)
# kq(2,3,mat)
# q_plus_kp(-1.5, 1, 4, mat)
# q_plus_kp(-2, 1, 5, mat)
# kq(2,4,mat)
# q_plus_kp(-1, 2, 3, mat)
# q_plus_kp((1/7), 2, 4, mat)
# kq(7,4,mat)
# q_plus_kp((4/7), 2, 5, mat)
# kq(7,5,mat)
# q_plus_kp(4, 3, 4, mat)
# q_plus_kp((-27/4), 3, 5, mat)
# kq(2,5,mat)
# q_plus_kp((-30/44), 4, 5, mat)
# kq(44,5,mat)

# x5 = mat[4,5]/mat[4,4]
# x4 = (mat[3,5] - (mat[3,4]*x5))/mat[3,3]
# x3 = (mat[2,5] - ((mat[2,4]*x5) + (mat[2,3]*x4)))/mat[2,2]
# x2 = (mat[1,5] - ((mat[1,4]*x5) + (mat[1,3]*x4) + (mat[1,2]*x3)))/mat[1,1]
# x1 = (mat[0,5] - ((mat[0,4]*x5) + (mat[0,3]*x4) + (mat[0,2]*x3) + (mat[0,1]*x2)))/mat[0,0]

# sol = np.array([x1, x2, x3, x4, x5])
# print(sol)

t = np.arange(1,10).reshape(3,3)
# print(t)

pqexchange(2,3,t)

# def simple_solver(augmat):
#     nrows = augmat.shape[0]
#     ncols = augmat.shape[1]
#     print('numrows:',nrows)
#     print('numcols:',ncols)
#     row = 1
#     while row < nrows:
#         augmat[row,0] !=0
#         factor = -1*(augmat[row,0]/augmat[row-1,0])
#         augmat = q_plus_kp(factor, row, row+1, augmat)
#         row += 1


""" 
let's write out the algorithm in words:

check 1st row -- element at 1,1 must not be 0
if not, we have to think about row operations to make exchanges
check 2nd row -- if 1st element is 0, go to next row, otherwise
    make 1st element in 2nd row 0
    return new matrix with updated second row
check 3rd row -- if 1st element is 0, go to next row, otherwise
    make 1st element in erd row 0
    return new matrix with updated 3rd row

    ...

repeat process until we have processed all rows in 1st colulmn. 

Then we check 2nd element in 2nd row to make sure it's not zero
so we are taking smaller and smaller submatrices and calling the same
relative operations on that submatrix

could probably implment some type of recursive function on this, it 
seems. 

 """


