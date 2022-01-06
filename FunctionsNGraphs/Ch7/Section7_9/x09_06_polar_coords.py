from x09_05_rotations_axes import *
from math import pi, exp

def plot_rtheta(r,theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

def midt(t1,t2):
    delta = (t2-t1)/2
    return t1+delta

# theta = np.linspace(0, pi)
# r = 4*np.sin(theta)

# x,y = plot_rtheta(r,theta)

# r2 = 2 + 2*np.cos(theta)
# plt.plot(*plot_rtheta(r2,theta)); plt.show()

def do_cardioid(a,b,trig_pos=True, cos=True):
    theta = np.linspace(0,2*pi)
    add = 1 if trig_pos else -1
    if cos:
        r = a + add*b*np.cos(theta)
    else:
        r = a + add*b*np.sin(theta)
    plt.plot(*plot_rtheta(r,theta))
    plt.show()

def do_cardioid_noshow(a,b,trig_pos=True, cos=True):
    theta = np.linspace(0,2*pi)
    add = 1 if trig_pos else -1
    if cos:
        r = a + add*b*np.cos(theta)
    else:
        r = a + add*b*np.sin(theta)
    plt.plot(*plot_rtheta(r,theta))

def do_four_leaf(a,b,n,f=1):
    # x = 2*n*2*pi if not n % 2 else n*2*pi
    # if n % 2 == 0:
    #     x = 2*n*2*pi
    # else:
    #     x = n*2*pi
    theta = np.linspace(0,2*pi,n)
    r = a*np.sin(b*theta)
    thetadeg = np.rad2deg(theta)
    print(
    f'''
    theta:\n{thetadeg[::(n//f)]}
    r:\n{r[::(n//f)]}   
    ''')
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return r,theta

strthetas = [
    '0', 
    'pi/6', 
    'pi/4', 
    'pi/3', 
    'pi/2', 
    '2*pi/3', 
    '3*pi/4', 
    '5*pi/6',
    'pi',
    '7*pi/6',
    '5*pi/4',
    '4*pi/3',
    '3*pi/2',
    '5*pi/3',
    '7*pi/4',
    '11*pi/6',
    '2*pi'
    ]

# rthetas = {}
# for stheta in strthetas:
#     theta = eval(stheta)
#     r = 2*np.sin(4*theta)
#     rthetas[stheta] = r

# print(rthetas)

# np.vstack((theta,r)).T  

def rtheta11(t1,t2, a=4,b=2,c=2,n=5):
    theta=np.linspace(t1,t2,n)
    r=(a*np.cos(b*theta))**(1/c)
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta 

def rtheta12(t1,t2, a=6,b=(1/2),c=1,n=5):
    theta=np.linspace(t1,t2,n)
    r = a*(np.sin(b*theta)**2)
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta 

def rtheta13(t1,t2, a=4,b=1,c=1,n=5):
    theta=np.linspace(t1,t2,n)
    r = a*(1/np.sin(b*theta))
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta 

def rtheta15(t1,t2, a=1,b=1,c=1,n=5):
    theta=np.linspace(t1,t2,n)
    r = 2 - (a*np.cos(b*theta))
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta, (r,theta) 

def sec(x):
    z =  np.cos(x)
    return 1/z

def rtheta16(t1,t2, a=1,b=1,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = 2 + 2*sec(theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta, (r,theta) 


# right function that plots the 4 quadrants, separtely!, not including undefined!


# 0-<90,>90-180, 180-<270,>270-360
# Q16:
# quardrant_bounds = [
#     (0,89.9),
#     (90.1,180),
#     (180,269.9),
#     (270.1,360)
# ]

# def deg2red_coors(d1,d2):
#     r1 = np.deg2rad(d1)
#     r2 = np.deg2rad(d2)
#     return r1,r2

# for q in quardrant_bounds:
#     r_theta, (r,theta) = rtheta16(*deg2red_coors(*q),n=1000)
#     x,y = plot_rtheta(r,theta)
#     plt.plot(x,y)

# plt.xlim(-1,5)
# plt.ylim(-5,5)
# plt.show()

# table16={}
# for x in range(0,365,5):
#     xrad = np.deg2rad(x)
#     table16[x]={f'cos({x})': np.cos(xrad), f'sec({x})': sec(xrad), f'2*sec({x})': 2*sec(xrad), f'2+2*sec({x})': (2*sec(xrad))+2}


def rtheta17(t1,t2, a=1,b=1,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = 2**theta
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta, (r,theta) 

def plot17(t1,t2,n=1000):
    r_theta, (r,theta) = rtheta17(t1,t2,n=n)
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

table17={}
for deg in range(0,375,15):
    theta = np.deg2rad(deg)
    r=2**theta
    table17[deg]={'r': f'{r}', 'x,y': plot_rtheta(r,theta)}



# q18 start:



def rtheta18(t1,t2, a=1,b=1,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = 1/theta
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta, (r,theta) 

def plot18(t1,t2,n=1000):
    r_theta, (r,theta) = rtheta18(t1,t2,n=n)
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

table18={}
for deg in range(5,365,5):
    if deg > 0:
        theta = np.deg2rad(deg)
        r=1/theta
        table18[deg]={'r': f'{r}', 'x,y': plot_rtheta(r,theta)}


# q18 end:


# q19 start:

def rtheta19(t1,t2, a=6,b=6,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = -a-(b*np.cos(theta))
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta, (r,theta) 

def plot19(t1,t2,n=1000):
    r_theta, (r,theta) = rtheta19(t1,t2,n=n)
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

table19={}
for deg in range(0,375,15):
    theta = np.deg2rad(deg)
    r=-6-(6*np.cos(theta))
    table19[deg]={'r': f'{r}', 'x,y': plot_rtheta(r,theta)}


# q19 end:


# q20 start:

def rtheta20(t1,t2, a=6,b=6,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = np.exp(2*theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T
    return r_theta, (r,theta) 

def plot20(t1,t2,n=1000):
    r_theta, (r,theta) = rtheta20(t1,t2,n=n)
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

table20={}
for deg in range(0,375,15):
    theta = np.deg2rad(deg)
    r=np.exp(2*theta)
    table20[deg]={'r': f'{r}', 'x,y': plot_rtheta(r,theta)}


# q20 end:




# q21 start:

def rtheta21(t1,t2, a=2,b=4,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = a + b*np.sin(theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table21={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2 = a + b*np.sin(theta2)
        table21[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table21 

def plot21(t1,t2,n=1000):
    x = rtheta21(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None




# q21 end:



# q22 start:

def rtheta22(t1,t2, a=8,b=5,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = a*np.cos(b*theta)
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table22={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2 = a*np.cos(b*theta2)
        table22[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table22 

def plot22(t1,t2,n=1000):
    x = rtheta22(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return x

def get_r22(deg,a=8,b=5):
    rad = np.deg2rad(deg)
    r = a*np.cos(b*rad)
    return r

# q22 end:



# q23 start:

def rtheta23(t1,t2, a=-16,b=2,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r2 =  a*np.sin(b*theta)
    # if r2 >= 0:
    r = r2**(1/2) 
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table23={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        _r2 = a*np.sin(b*theta)
        r2 = _r2**(1/2) 
        table23[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table23 

def plot23(t1,t2,n=1000):
    x = rtheta23(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def get_r23(deg,a=8,b=5):
    rad = np.deg2rad(deg)
    r2 =  a*np.sin(b*rad)
    r = sqrt(r2)
    return r

# q23 end:





# q24 start:

def rtheta24(t1,t2, a=-16,b=2,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = theta/4
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table24={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2 = theta2/4
        table24[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table24 

def plot24(t1,t2,n=1000):
    x = rtheta24(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def get_r24(deg,a=8,b=5):
    rad = np.deg2rad(deg)
    r=rad/4
    return r

# q24 end:







# q36 start:

def rtheta36(t1,t2, a=-16,b=2,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r= 6*(np.cos(theta)/np.sin(theta))
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table36={}
    for deg in range(5,365,5):
        theta2 = np.deg2rad(deg)
        r2 = 6*(np.cos(theta2)/np.sin(theta2))
        table36[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table36 

def plot36(t1,t2,n=1000):
    x = rtheta36(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def plot36_noshow(t1,t2,n=1000):
    x = rtheta36(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    return None

def get_r36(deg,a=8,b=5):
    rad = np.deg2rad(deg)
    r = 6*(np.cos(rad)/np.sin(rad))
    return r

def points36(precision):
    possible_points = []
    for y in range(100):
        for x in range(100):
            a=y**2
            b=x**2
            try:
                z = (a*(a+b))/b
                if abs(36 - z) < precision:
                    print(z)
                    possible_points.append((x,y))
            except:
                continue    
    return possible_points


# q36 end:



# q48 start:

def rtheta48(t1,t2, a=-16,b=2,c=1,n=5):
    '''conchoid'''
    theta=np.linspace(t1,t2,n)
    r = 4/(2+(np.sin(theta)))
    r_theta=np.vstack((np.rad2deg(theta),r)).T

    table48={}
    for deg in range(0,375,15):
        theta2 = np.deg2rad(deg)
        r2 = 4/(2+(np.sin(theta2)))
        table48[deg]={'r': f'{r2}', 'x,y': plot_rtheta(r2,theta2)}

    return r_theta, (r,theta), table48 

def plot48(t1,t2,n=1000):
    x = rtheta48(t1,t2,n=n)
    r = x[1][0]
    theta = x[1][1]
    plt.plot(*plot_rtheta(r,theta))
    plt.show()
    return None

def get_r48(deg,a=8,b=5):
    rad = np.deg2rad(deg)
    r = 4/(2+(np.sin(rad)))
    return r

# q48 end:



def ret_bin8(x):
    binlen = len(bin(x)[2:])
    leadzero = '0'*(8-binlen)
    return leadzero + bin(x)[2:]

# x = [(i, bin(i), hex(i)) for i in range(31)]
# for i,j,k in x:
#     print(f'dec: {i:>2}, bin: {j[2:]:>5}, hex: {k[2:]:>2}')
    
def ret_binop(x,y):
    print(f"""
    bin(x):             {ret_bin8(x):>8}
    x:                  {x:>8}
    
    bin(y):             {ret_bin8(y):>8}
    y:                  {y:>8}
    
    binary AND (x & y): {ret_bin8(x & y):>8}
    binary AND as dec:  {x & y:>8}
    
    binary OR (x | y):  {ret_bin8(x | y):>8}
    binary OR as dec:   {x | y:>8}
    
    binary XOR (x ^ y): {ret_bin8(x ^ y):>8}
    binary XOR as dec:  {x ^ y:>8}
    """)
    return None

def print_polarcoords(t,r,n,m):
    print(f'{t:>{n}}: {r:>{m}.2f}')
    return None
