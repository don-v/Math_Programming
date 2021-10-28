import numpy as np
from numpy.linalg import det
from chapter7_funcs_src import *

# A22 = mat_maker((4,4), 3,2,0,4, -2,0,5,0, 4,-3,1,6, 2,-1,2,0)
# print(det(A22))

# A23 = mat_maker((5,5), 2,-2,0,0,-3, 3,0,3,2,-1, 0,1,-2,0,2, -1,2,0,3,0, 0,4,1,0,0)
# print(det(A23))

A24 = mat_maker((5,5), 2,0,-1,0,2, 1,3,0,0,1, 0,4,3,0,-1, -1,2,0,-2,0, 0,1,5,0,-4)
print(det(A24))