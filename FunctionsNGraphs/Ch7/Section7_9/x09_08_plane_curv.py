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
    curve_points[c] = theory_ex3(-2,2,c[0],c[1],n=1000)

# for c in curve_points.items():
#     print(c)

def param_plot_nosho(points_dict):
    plt.xlim(0,4)
    plt.ylim(-2,2)
    for p in points_dict.values():
        plt.plot(*p,marker='o',c='c')
    return None 

# for point_dict in curve_points.values():
#     param_plot_nosho(point_dict)
# plt.show()

def four_plot(points_dict,curves):
    len_pd = len(points_dict)
    for i in range(len_pd):
        plt.subplot(2,2,i+1)
        for p in points_dict[curves[i]].values():
            plt.xlim(0,4)
            plt.ylim(-2,2)
            plt.plot(*p,marker='o', c='c')
    return None


def four_plot24(a,b,n):
    C1 = ('t', '1-t')
    C2 = ('1-(t**2)', 't**2')
    C3 = ('(np.cos(t))**2', '(np.sin(t))**2')
    C4 = ('(np.log(t))-t'), '1+t-(np.log(t))'

    curves = [C1,C2,C3,C4]

    curve_points = {}
    for c in curves:
        if c == C4:
            curve_points[c] = theory_ex3(0.0000000001,b,c[0],c[1],n=n)
        else:
            curve_points[c] = theory_ex3(a,b,c[0],c[1],n=n)


    len_pd = len(curve_points)
    for i in range(len_pd):
        plt.subplot(2,2,i+1)
        for p in curve_points[curves[i]].values():
            plt.plot(*p,marker='o', c='c')
    return curves, curve_points

    # adjust n tomorrow! 
    