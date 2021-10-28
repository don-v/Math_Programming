import numpy as np  
import matplotlib.pyplot as plt  
from chapter7_funcs_src import *

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)  
    plt.show()  

def my_formula(x):
    return x**3+2*x-4

# graph(my_formula, range(-10, 11))

zymat = mat_maker((4,3), 0.2,0.1,2.8, 0.4,0.2,3.2, 0.15,0.25,4, 1,1,20)

def simple_exp(na):
    expr = (na[2]-na[1])/na[0]
    print(expr)
    return expr

for row in range(zymat.shape[0]):
    simple_exp(zymat[row,:])
