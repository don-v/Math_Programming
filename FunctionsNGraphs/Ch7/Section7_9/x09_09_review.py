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

def prt27_0(t1,t2,n=5):
    x = rtheta27r(t1,t2,n=n)
    return x[0]

def prt27_1(t1,t2,n=5):
    x = rtheta27r(t1,t2,n=n)
    return x[1]

def prt27_2(t1,t2,n=5):
    x = rtheta27r(t1,t2,n=n)
    for k,v in x[2].items():
        print(f"{k:>5}: {eval(v['r']):>5.2f}")
    return x[2] 



# q27r end:




# q28r start:

def rtheta28r(t1,t2, a=9,b=2,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    z =  a*np.sin(b*theta)
    z[z<0] = np.nan
    r = z**(1/2) 
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table28r={}
    for deg in range(0,361):
        theta2 = np.deg2rad(deg)
        z2 = a*np.sin(b*theta2)
        z3 = z2 if z2 >=0 else np.nan
        r2 = z3**(1/2) 
        table28r[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table28r 

def plot28r(t1,t2,n=1000):
    x = rtheta28r(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def get_r28r(deg,a=9,b=2):
    rad = np.deg2rad(deg)
    r2 =  a*np.sin(b*rad)
    r = sqrt(r2)
    return r



def prt28_0(t1,t2,n=5):
    x = rtheta28r(t1,t2,n=n)
    return x[0]

def prt28_1(t1,t2,n=5):
    x = rtheta28r(t1,t2,n=n)
    return x[1]

def prt28_2(t1,t2,n=5):
    x = rtheta28r(t1,t2,n=n)
    for k,v in x[2].items():
        # conditional execute if v ^= 'nan'
        sr = v['r'] if v['r'] == 'nan' else f"{eval(v['r']):>5.2f}"
        print(f"{k:>5}: {sr}")
    return x[2] 


# q28r end:


# q29r start:

def rtheta29r(t1,t2,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r=theta/2
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table29r={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2=theta2/2 
        table29r[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table29r 

def plot29r(t1,t2,n=1000):
    x = rtheta29r(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def get_r29r(deg):
    rad = np.deg2rad(deg)
    r = rad/2
    return r

def prt29_0(t1,t2,n=5):
    x = rtheta29r(t1,t2,n=n)
    return x[0]

def prt29_1(t1,t2,n=5):
    x = rtheta29r(t1,t2,n=n)
    return x[1]

def prt29_2(t1,t2,n=5):
    z = rtheta29r(t1,t2,n=n)
    for k,v in z[2].items():
        r = eval(v['r'])
        x,y = v['x,y']
        print(f"{k:>5}: r={r:>5.2f}, x,y={x:>5.2f},{y:>5.2f}")
    return z[2] 


# q29r end:

# q41r start:

def param_plot(points_dict):
    for p in points_dict.values():
        plt.plot(*p,marker='o', color='c')
    plt.show()

def ex41r(a,b,xexp:str, yexp:str,n=50,byk=False):
    points_dict = {}
    for t in np.linspace(a,b,n):
        if abs(t) >0:
            x = eval(xexp) 
            y = eval(yexp)
            points_dict[t] = (x,y)
    sorted_x = sorted(points_dict.items(), key=lambda kv: kv[1][0])
    if byk: return points_dict
    return sorted_x


# x=ex41r(0,4,'(1/t)+1','(2/t)-t',9)  
# for k,v in x.items():
#     print(f"{k:>5.2f}: {v[0]:>5.2f},{v[1]:>5.2f}")
# param_plot(x)


def prt_ex41r(points_dict):
    if isinstance(points_dict, dict):
        for k,v in points_dict.items():
            print(f"{k:>5.2f}: {v[0]:>5.2f},{v[1]:>5.2f}")
    else:
        for tup in points_dict:
            print(f"{tup[0]:>5.2f}: {tup[1][0]:>5.2f},{tup[1][1]:>5.2f}")



# q41r end:








