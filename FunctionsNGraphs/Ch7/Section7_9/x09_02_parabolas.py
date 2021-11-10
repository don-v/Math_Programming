from x07_10_review import *
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import re 


def display_sign(x):
    sign = '+' if x < 0 else '-'
    return sign

def display_hkp(x):
    display_p = -x if x < 0 else x
    return display_p

def get_plotvars(a,b,c, vertical=True, xlim=(-10,10)):
    x = np.arange(xlim[0],xlim[1] + .001,.001)
    y = (a*(x**2)) + (b*x) + c
    return (x,y) if vertical else (y,x)
    

def plot_parabola(x,y,xlim,ylim):
    plt.plot(x,y)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim)
    plt.vlines(0, *ylim)
    plt.show()
    return None 

# def plot_annotate(h,k,p):
#     plt.annotate('Vertex', (h,k), xytext=(h-.1, k-.1))
#     plt.annotate('Focus', )
#     plt.show()


def get_hkp(a,b,c, vertical=True):
    """Extract the parameters h, k, p from a
    parabolic equation of the form y = ax^2 + bx + c"""

    h = -1*(b/(2*a))
    k = c-((b**2)/(4*a))
    p = 1/(4*a)

    return (h,k,p) if vertical else (k,h,p)

def ret_VFDx(h,k,p, vertical=True):
    """
    The graph of each of the following equations is a 
    parabola that has vertex V(h,k) and indicated focus
    and directrix:

    (i). equation: (x-h)^2 = 4p(y-k)
    vertex: (h,k)
    focus: (h, k+p)
    directrix: y = k-p

    (ii). equation: (y-k)^2 = 4p(x-h)
    vertex: (h,k)
    focus: (h+p, k)
    directrix: x = h-p    
    """
    V = (h,k)
    
    if vertical:
        F = (h, k+p)
        Dx = f'y = {k} {display_sign(p)} {display_hkp(p)}'
        equation = f'(x {display_sign(h)} {display_hkp(h)})**2 = 4*{p}*(y {display_sign(k)} {display_hkp(k)})'
    
    else:
        F = (h+p, k)
        Dx = f'x = {h} {display_sign(p)} {display_hkp(p)}'
        equation = f'(y {display_sign(k)} {display_hkp(k)})**2 = 4*{p}*(x {display_sign(h)} {display_hkp(h)})'

    direction = 'vertical' if vertical else 'horizontal'

    return (V, F, Dx, equation, direction)

def eval_Dx(streq):
    x = re.search('-\d.*$|\d.*$', streq)
    return eval(x.group(0))



def do_parabola(a,b,c,vertical=True, xlim=(-100,100), ylim=(-100,100)):
    hkp = get_hkp(a,b,c,vertical)
    vertex, focus, Dx, eq, direction = ret_VFDx(*hkp, vertical)
    print(f'vertex: V{vertex}')
    print(f'focus: F{focus}')
    xyvar = 'y' if vertical else 'x'
    print(f'Dx: {xyvar} = {eval_Dx(Dx)}')
    plotvars = get_plotvars(a,b,c,vertical,xlim)
    plt.plot(*plotvars)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.hlines(eval_Dx(Dx), *xlim) if vertical else plt.vlines(eval_Dx(Dx), *ylim)
    plt.annotate(
        f'Vertex: V{vertex}', 
        vertex,
        xycoords='data',
                  xytext=(1,1), textcoords='axes fraction',
                  size=20, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  fc="w"),
        )
    
    plt.annotate(
        f'Focus: F{focus}', 
        focus,
        xycoords='data',
                  xytext=(1, 0.5), textcoords='axes fraction',
                  size=20, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  fc="w"),
        )

    directrix_xy = (eval_Dx(Dx), hkp[1]) if not vertical else (hkp[0], eval_Dx(Dx))


    plt.annotate(
        f'Directrix: {xyvar} = {eval_Dx(Dx)}', 
        directrix_xy,
        xycoords='data',
                  xytext=(1, 0), textcoords='axes fraction',
                  size=20, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  fc="w"),
        )


    plt.show()
    
def do_parabola_noshow(a,b,c,vertical=True, xlim=(-100,100), ylim=(-100,100)):
    hkp = get_hkp(a,b,c,vertical)
    vertex, focus, Dx, eq, direction = ret_VFDx(*hkp, vertical)
    print(f'vertex: V{vertex}')
    print(f'focus: F{focus}')
    xyvar = 'y' if vertical else 'x'
    print(f'Dx: {xyvar} = {eval_Dx(Dx)}')
    plotvars = get_plotvars(a,b,c,vertical,xlim)
    plt.plot(*plotvars)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.hlines(eval_Dx(Dx), *xlim) if vertical else plt.vlines(eval_Dx(Dx), *ylim)
    return None


def do_parabola_(a,b,c,vertical=True, xlim=(-100,100), ylim=(-100,100)):
    hkp = get_hkp(a,b,c,vertical)
    vertex, focus, Dx, eq, direction = ret_VFDx(*hkp, vertical)
    print(f'vertex: V{vertex}')
    print(f'focus: F{focus}')
    xyvar = 'y' if vertical else 'x'
    print(f'Dx: {xyvar} = {eval_Dx(Dx)}')
    plotvars = get_plotvars(a,b,c,vertical,xlim)
    plt.plot(*plotvars)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.hlines(eval_Dx(Dx), *xlim) if vertical else plt.vlines(eval_Dx(Dx), *ylim)
    plt.show()
    return None

    

    

