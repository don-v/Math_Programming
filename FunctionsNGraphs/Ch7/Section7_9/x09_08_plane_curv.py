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

def theory_ex17(a,b,xexp:str, yexp:str,n=50):
    points_dict = {}
    for t in np.linspace(a,b,n):
        if abs(t) >=1:
            x = eval(xexp) 
            y = eval(yexp)
            points_dict[t] = (x,y)
    return points_dict

def theory_ex18(a,b,xexp:str, yexp:str,n=50):
    points_dict = {}
    for t in np.linspace(a,b,n):
        if abs(t) <=1:
            x = eval(xexp) 
            y = eval(yexp)
            points_dict[t] = (x,y)
    return points_dict

def theory_ex22(a,b,xexp:str, yexp:str,n=50):
    points_dict = {}
    for t in np.linspace(a,b,n):
        if t > -pi/2 and t < pi/2:
            x = eval(xexp) 
            y = eval(yexp)
            points_dict[t] = (x,y)
    return points_dict

C1 = ('t**2', 't')
C2 = ('t**4', 't**2')
C3 = ('(np.sin(t))**2', 'np.sin(t)')
C4 = ('np.exp(2*t)'), '-1*(exp(t))'

curves = [C1,C2,C3,C4]

curve_points = {}
for c in curves:
    curve_points[c] = theory_ex3(-5,5,c[0],c[1],n=10)

# for c in curve_points.items():
#     print(c)

def param_plot_nosho(points_dict):
    for p in points_dict.values():
        plt.plot(*p,marker='o')
    return None 

# for point_dict in curve_points.values():
#     param_plot_nosho(point_dict)
# plt.show()
