"""
A function f is a polynomial if:

f(x) = a_{n}*x**n + a_{n-1}*x**(n-1) + ... + a_{1}*x + a_{0}

where the coefficients a_{0}, a_{1}, ... , a_{n} are real numbers and
the exponents are nonnegative integers

"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def gen_coeffs(n=2):
    coeffs = dict()
    for x in range(n+1):
        coeffs[f'a{x}'] = float(input(f'the value of a{x} is: '))
    return coeffs

def gen_poly(n=2):
    if n==0: return f"c[f'a{n}']*x**{n}"
    else: return f"c[f'a{n}']*x**{n}" + ' + ' + gen_poly(n-1)

def poly_display(c:dict, n=2):
    if n==0: return f"{c[f'a{n}']:.2f}*x**{n}"
    else: return f"{c[f'a{n}']:.2f}*x**{n}" + ' + ' + poly_display(c,n-1)
   
def eval_poly(p:str, c:dict, rangex:tuple, lst=None):
    points = dict()
    if not lst:
        for x in range(*rangex):
            points[x] = eval(p)
        return points
    else:
        for x in lst:
            points[x] = eval(p)
        return points

def plot_poly(c:dict):
    plt.plot(*zip(*sorted(c.items()))); plt.show()
    return None  

def poly_pts_plot(n,rangex=None,lst=[-2,1,0,1,2],plot=True):
        c = gen_coeffs(n)
        p = gen_poly(n)
        points = eval_poly(p,c,rangex,lst=lst)
        if plot:
            plot_poly(points)  
            return points
        return points

def ax_tothe_n(a,n,pos=True,plot=False):
    sign = 1 if pos else -1
    x=np.linspace(-5,5,1000)
    y=sign*a*(x**n)
    plt.plot(x,y)
    if plot: 
        plt.show()
        return None
    return None

def n4_ax_tothe_n(a=1,n_=10,pos=True):
    inc = 1 if n_<10 else n_//10
    for i in range(0,n_,inc):
        ax_tothe_n(a,i,pos)
    plt.show()
    return None

def a4_ax_tothe_n(a=10,n_=3,pos=True):
    inc = 1 if a<10 else a//10
    for i in range(0,a,inc):
        ax_tothe_n(i,n_,pos)
    plt.show()
    return None


if __name__ == '__main__':
    if len(sys.argv) == 1:
        c = gen_coeffs()
        p = gen_poly()
        d = poly_display(c)
        points = eval_poly(p,c,(-5,6))
        print(f"""
        n={2}
        polynomial={d}
        points = {points}
        """)
        plot_poly(points)
    else:
        n = int(sys.argv[1])
        c = gen_coeffs(n)
        p = gen_poly(n)
        d = poly_display(c,n)
        points = eval_poly(p,c,(-5,6))
        print(f"""
        n={n}
        polynomial={d}
        points = {points}
        """)
        plot_poly(points)

