from chapter7_funcs_src import *
from itertools import combinations
from numpy.linalg import det

def solve_at_once(mat):
    x = echelon_solver(to_echelon(mat))
    print('the solution is:', x[1])

# A1 = mat_maker2((2,3), 2,-3,4, 5,4,1)
# solve_at_once(A1)

def ret_xy_intercept(a,b,c):
    yint = 0, c/b
    xint = c/a, 0
    return (xint, yint)

def get_all_xyints(mat):
    xyints = {}
    for row in range(3):
        a,b,c = tuple(mat[row, :])
        # print(f"""
        # row = {row}
        # mat[row, :] = {mat[row,:]}
        # tuple(mat[row,:]) = {tuple(mat[row,:])}

        # a = {a}
        # b = {b}
        # c = {c}
               
        # """)
        xyints[row] = ret_xy_intercept(a,b,c)
    return xyints

def sel_rows(tup, mat):
    return mat[tup, :]

def solve_all2(mat,n):
    sols = {}
    mat_combos = combinations(range(n), 2)
    # combos = [x for x in list(mat_combos) if x[1] == 3]
    for combo in mat_combos:
        sols[combo] = echelon_solver(to_echelon(sel_rows(combo, mat)))[1]
    print(sols)
    return sols

# A19 = mat_maker2((3,3), 1,-2,2, -3,1,4, 2,1,4)
# xyints = get_all_xyints(A19)
# sols = solve_all2(A19,3)
# print('xyints:',xyints)
# print('sols:', sols)


def ret_qeq(a,b,c):
    disc = ((b**2)-(4*a*c))**(1/2)
    x1 = ((-1*b)+disc)/(2*a)
    x2 = ((-1*b)-disc)/(2*a) 
    return (x1,x2)

def ret_posneg_x(y):
    tmp = y**(1/2)
    x1,x2 = -tmp, tmp
    return (x1,x2)


# we want to write functions for determinants, minors, and cofactors for squre matrix!

def ret_minor_size(mat,m,n):
    tmpr = np.delete(mat, m-1, 0)
    tmpc = np.delete(tmpr,n-1,1)

    # print(f"""
    # inside ret_minor_size:
    # mat = \n\n{mat}
    # m = {m}
    # n = {n}
    # tmpr = \n\n{tmpr}
    # tmpc = \n\n{tmpc}
    # """)

    return tmpc

def cofactor(mat, m, n):
    sign = 1 if (m + n) % 2 == 0 else -1
    
    # print(f"""
    # inside cofactor:
    # mat = \n\n{mat}
    # m = {m}
    # n = {n}
    # sign = {sign}
    # """)
    
    return sign*ret_det(mat)

def ret_det(mat):
    # m,n = mat.shape
    # print(f"""
    
    # inside ret_det, before if clause:
    # mat = \n\n{mat}
    
    # """)
    if (mat.shape[0] == mat.shape[1] & mat.shape[0] == 2):
        det22 =  (mat[0,0]*mat[1,1]) - (mat[0,1]*mat[1,0])
        # print('det22:', det22)
        return det22
    else:
        det = 0
        for i in range(mat.shape[1]):

            # print(f"""
            # inside else, before computations in for loop:
            
            # i={i}
            # det={det}
            # """)

            submat = ret_minor_size(mat,1,i+1)
            comp = mat[0,i]*cofactor(submat, 1, i+1)
            # print(f"""
            # inside else, after submat, before det sum
            
            # submat = \n\n{submat}
            # i={i}
            # det={det}
            # mat[0,i] = {mat[0,i]}
            # cofactor(submat, 1, i+1) = {cofactor(submat, 1, i+1)}
            # ret_det(submat) = {ret_det(submat)}
            # comp = {comp}
            # """) 

            det += comp

            # print(f"""
            # inside else, after computations in for loop:
            
            # submat = \n\n{submat}
            # i={i}
            # det={det}
            # """)            
        return det


        

# for a 3,3, we take the 1st row,  a11*cofactora11 + a12*cofactora12 + a13*cofactora13


# test_mat = np.array([[3,-4], [6,8]])
# print(f"""

# test_mat = {test_mat}
# ret_det(test_mat) = {ret_det(test_mat)}
# numpy.linalg.det(test_mat) = {det(test_mat)}

# """)

# test_33 = mat_maker2((3,3), -1,3,1, 2,5,0, 3,1,-2)
# print(f"""

# test_mat = {test_33}
# ret_det(test_33) = {ret_det(test_33)}
# numpy.linalg.det(test_33) = {det(test_33)}

# """)


# A24 = mat_maker2((3,3), 0,4,-3, 2,0,4, -5,1,0)
# print(f"""

# test_mat = {A24}
# ret_det(A24) = {ret_det(A24)}
# numpy.linalg.det(A24) = {det(A24)}

# """)

def print_dets(mat):
    x = f"""
original_matrix:
{mat}
    
my det function!: = {ret_det(mat)}
numpy.linalg.det: = {det(mat)}"""
    print(x)
    return None 


def ret_inv(mat):
    inverse_solver(augmented_matrix_maker(mat))
    return None


def inv_22_form(mat):
    a,b,c,d = mat[0,0], mat[0,1], mat[1,0], mat[1,1]
    det = (a*d)-(b*c)
    a_ = ((a*b*c) + (a*d) - (b*c))/a
    b_ = -b
    c_ = (-1)*a*c
    d_ = a
    return np.array([[(a_/det),(b_/det)],[(c_/det),(d_/det)]])

# result = inv_22_form(mat_maker2((2,2), 1,2,3,4))
# print(result)