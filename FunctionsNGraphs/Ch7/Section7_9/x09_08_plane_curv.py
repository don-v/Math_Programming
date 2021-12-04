from x09_07_polar_conics import *

def theory_ex1(a,b, xexp:str, yexp:str):
    points_dict = {}
    for t in range(a,b+1):
        x = eval(xexp) 
        y = eval(yexp)
        points_dict[t] = (x,y)
    return points_dict

def cube(x):
    if 0<=x: return x**(1./3.)
    return -(-x)**(1./3.)

def theory_ex1_(a,b, xexp:str, yexp:str):
    points_dict = {}
    for t in range(a,b+1):
        t = cube(t)
        x = eval(xexp) 
        y = eval(yexp)
        points_dict[t] = (x,y)
    return points_dict

def theory_ex3(a,b,xexp:str, yexp:str,n=50):
    points_dict = {}
    for t in np.linspace(a,b,n):
        x = eval(xexp) 
        y = eval(yexp)
        points_dict[t] = (x,y)
    return points_dict

def param_plot(points_dict):
    for p in points_dict.values():
        plt.plot(*p,marker='o', color='c')
    plt.show()