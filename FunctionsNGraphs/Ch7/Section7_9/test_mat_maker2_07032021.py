from chapter7_funcs_src import *
from math import log, log10

# A1 = mat_maker2((2,3), 2,-3,4, 5,4,1)
# # print(A1)

# A1ech = to_echelon(A1)
# # print(A1ech)

# A1sol = echelon_solver(A1ech)
# print(A1sol)

def ret_inv(x):
    return 1/x

def ret_x(x_prime):
    x = log(x_prime)/log(2)
    return x

def ret_y(y_prime):
    y = log(y_prime)/log(3)
    return y

def ret_qeq(a,b,c):
    disc = (b**2-(4*a*c))**(1/2)
    x1 = ((-1*b)+disc)/2*a
    x2 = ((-1*b)-disc)/2*a 
    return (x1,x2)
    # print(f"""
    # a = {a}
    # b = {b}
    # c = {c}

    # -b = {-b}
    # b**2 = {b**2}
    # 4*a*c = {4*a*c}
    # 2*a = {2*a}    

    # b2-4ac**(1/2) = {((b**2)-(4*a*c))**(1/2)}
    # -b + b2-4ac**(1/2)/2*a = {(-b + (((b**2)-(4*a*c))**(1/2)))/2*a}
    # -b - b2-4ac**(1/2)/2*a = {(-b - (((b**2)-(4*a*c))**(1/2)))/2*a}
    # """)

# print(ret_qeq(1,1,-16))

def ret_posneg_x(y):
    tmp = y**(1/2)
    x1,x2 = -tmp, tmp
    return (x1,x2)



