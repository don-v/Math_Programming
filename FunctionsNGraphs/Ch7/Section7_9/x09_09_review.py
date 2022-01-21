from x09_08_plane_curv import *

# def param_plot(points_dict):
#     for p in points_dict.values():
#         plt.plot(*p,marker='o', color='c')
#     plt.show()

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


def prt_ex41r(points_dict):
    if isinstance(points_dict, dict):
        for k,v in points_dict.items():
            print(f"{k:>5.2f}: {v[0]:>5.2f},{v[1]:>5.2f}")
    else:
        for tup in points_dict:
            print(f"{tup[0]:>5.2f}: {tup[1][0]:>5.2f},{tup[1][1]:>5.2f}")



def q41r_rect(a=1.25,b=10,n=50):
    x = np.linspace(a,b,n)
    y = ((2*((x-1)**2))-1)/(x-1)
    return x,y

# q41r end:



# q42r start:

def ex42r(a,b,xexp:str, yexp:str,n=50,byk=False):
    points_dict = {}
    for t in np.linspace(a,b,n):
        x = eval(xexp) 
        y = eval(yexp)
        points_dict[t] = (x,y)
    sorted_x = sorted(points_dict.items(), key=lambda kv: kv[1][0])
    if byk: return points_dict
    return sorted_x


def prt_ex42r(points_dict):
    if isinstance(points_dict, dict):
        for k,v in points_dict.items():
            print(f"{k:>5.2f}: {v[0]:>5.2f},{v[1]:>5.2f}")
    else:
        for tup in points_dict:
            print(f"{tup[0]:>5.2f}: {tup[1][0]:>5.2f},{tup[1][1]:>5.2f}")



def q42r_rect(a=0,b=2,n=50):
    y = np.linspace(a,b,n)
    x = ((-1*(y**2)) + (2*y)) - 2
    return x,y

# q42r end:


# q43r start:

def ex43r(a,b,xexp:str, yexp:str,n=50,byk=False):
    points_dict = {}
    for t in np.linspace(a,b,n):
        x = eval(xexp) 
        y = eval(yexp)
        points_dict[t] = (x,y)
    sorted_x = sorted(points_dict.items(), key=lambda kv: kv[1][0])
    if byk: return points_dict
    return sorted_x


def prt_ex43r(points_dict):
    if isinstance(points_dict, dict):
        for k,v in points_dict.items():
            print(f"{k:>5.2f}: {v[0]:>5.2f},{v[1]:>5.2f}")
    else:
        for tup in points_dict:
            print(f"{tup[0]:>5.2f}: {tup[1][0]:>5.2f},{tup[1][1]:>5.2f}")



def q43r_rect(a=0,b=10,n=50):
    x = np.linspace(a,b,n)
    xsq = x**2
    negxsq = -1*xsq
    y = 2**(negxsq)
    return x,y

# q43r end:


# q44r start:

def four_plot44r(a,b,n):
    C1 = ('t', 'sqrt(t)')
    C2 = ('t**2', 't')
    C3 = ('1-((np.sin(t))**2)', 'np.cos(t)')
    C4 = ('np.exp(2*t)','-1*np.exp(t)')

    curves = [C1,C2,C3,C4]

    curve_points = {}
    for c in curves:
        if c == C1:
            curve_points[c] = theory_ex3(0.0000000001,b,c[0],c[1],n=n)
        else:
            curve_points[c] = theory_ex3(a,b,c[0],c[1],n=n)


    len_pd = len(curve_points)
    for i in range(len_pd):
        plt.subplot(2,2,i+1)
        for p in curve_points[curves[i]].values():
            plt.plot(*p,marker='o', c='c')
    return curves, curve_points

# q44r end:

# q45r -- need to update cos2phi in rotaiton_axes.py!

def get_degphi(x, sin=True):
    rad = np.arcsin(x) if sin else np.arccos(x)
    deg = np.rad2deg(rad)
    return deg
