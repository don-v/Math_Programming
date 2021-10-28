import numpy as np
from numpy.linalg import det
from chapter7_funcs_src import *

def cramer(mat):
    print('mat:', mat)
    x = np.ones(mat.shape[0])
    x[:] = np.NaN
    print("x:", x)
    detDis = np.copy(x)
    D = mat[:, :-1]
    print("D:", D)
    
    for i in range(x.size):
        Di = D.copy()
        Di[:,i] = mat[:,-1]
        detDis[i] = det(Di)
        print('Di:',Di)
        if det(D) !=0:
            x[i] = det(Di)/det(D)
        else:
            pass
        
    if det(D) != 0:    
        print('there is precisely 1 solution:',x)
        print('the set of determinants:', detDis)
        return (x, detDis, D)
    else:
        if all(detDis == 0):
            print('there are infinitely many solutions')
            return None
        else:
            print('there are no solutions')
            return None

def sr(x):
    '''return square root of argument'''
    return x**(1/2)
    
def build_Dis(mat):
    D = mat[:, :-1]
    Dis = {}
    for i in range(mat.shape[1]-1):
        x = 'D'+str(i)
        Di = D.copy()
        Di[:,i] = mat[:,-1]
        Dis[x] = Di

    print(Dis)    
    return(Dis)

def print_detmats(dict_dets):
    for k,v in dict_dets.items():
        print(f'det mats {k}:\n',v)
        print(f'dets {k}:\n',det(v))
    
