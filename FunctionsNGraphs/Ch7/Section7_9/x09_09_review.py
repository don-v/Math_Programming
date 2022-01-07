from x09_08_plane_curv import *

# q26r start:

def rtheta26r(t1,t2, a=3,b=5,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = a*np.sin(b*theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table26r={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2 = a*np.sin(b*theta2)
        table26r[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table26r 

def plot26r(t1,t2,n=1000):
    x = rtheta26r(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return x

def get_r26r(deg,a=3,b=5):
    rad = np.deg2rad(deg)
    r = a*np.sin(b*rad)
    return r


# >>> def print_x0(t1,t2):
# ...     x=rtheta26r(t1,t2)
# ...     return x[0]
# ... 
# >>> def print_x1(t1,t2):   
# ...     x=rtheta26r(t1,t2)
# ...     return x[1] 
# ... 
# >>> def print_x2(t1,t2):   
# ...     x=rtheta26r(t1,t2)
# ...     return x[2] 

# q26r end: