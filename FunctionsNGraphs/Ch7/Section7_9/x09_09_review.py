from x09_08_plane_curv import *

# q26r start:

def rtheta26r(t1,t2, a=3,b=5,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = a*np.cos(b*theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table26r={}
    for deg in range(0,378,18):
        theta2 = np.deg2rad(deg)
        r2 = a*np.cos(b*theta2)
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


def print_x0(t1,t2):
    x=rtheta26r(t1,t2)
    return x[0]
 
def print_x1(t1,t2):   
    x=rtheta26r(t1,t2)
    return x[1] 
 
def print_x2(t1,t2):   
    x=rtheta26r(t1,t2)
    for k,v in x[2].items():
        print(f"{k:>5}: {eval(v['r']):>5.2f}")
    return x[2] 

# q26r end:


# q27r start:

def rtheta27r(t1,t2, a=6,b=3,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = a - b*np.cos(theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table27r={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2 = a - b*np.cos(theta2)
        table27r[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table27r 

def plot27r(t1,t2,n=1000):
    x = rtheta27r(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def prt27(t1,t2,n=5):
    pass


# q27r end:
