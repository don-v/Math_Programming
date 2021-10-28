from matplotlib.pyplot import yscale
from x09_04_hyperbolas import *

# section95_mat = mat_maker2((3,3), 9,-24,16, 12,-7,-12, 16,24,9)
# # section95_mat[0,:]

# mult = np.array([41,-24,34])
# result_mat = np.ones((3,3))
# for i in range(section95_mat.shape[0]):
#     print(f'row {i}: {section95_mat[i,:]*mult[i]}')
#     result_mat[i] = section95_mat[i,:]*mult[i]
# print(result_mat.sum(axis=0))

def eqn_to_cos2phi(a,b,c,d,e,f):
    if b !=0:
        cos2phi = (a-c)/b
        return cos2phi

def rot_axes(cos2phi):
    sinphi = sqrt((1-cos2phi)/2)
    cosphi = sqrt((1+cos2phi)/2)
    # xcoeff = (cosphi, -sinphi)
    # ycoeff = (sinphi, cosphi)
    # xpcoef = (cosphi, sinphi)
    # ypcoef = (-sinphi, cosphi)
    return cosphi, sinphi

def binom_x2y2(a,b,x=True):
    if x:
        b = -b
        return a**2, 2*a*b, b**2
    else:
        return b**2, 2*a*b, a**2

def binom_xy(a,b):
    return a*b, (a**2 - b**2), -1*a*b

def rotated_coeffs(a,b,c,d,e,f):
    result_mat = np.ones((3,3))
    mult = np.array([a,b,c])
    co,si = rot_axes(eqn_to_cos2phi(a,b,c,d,e,f))
    cm = mat_maker2((3,3), *binom_x2y2(co,si), *binom_xy(co,si), *binom_x2y2(co,si,False))
    for i in range(cm.shape[0]):
        print(f'row {i}: {cm[i,:]*mult[i]}')
        result_mat[i] = cm[i,:]*mult[i]
    print(result_mat.sum(axis=0))
    return result_mat.sum(axis=0)

def whole_number_equation_sub(a,b,c,d,e,f,xpc,ypc,denom=25):
    mult = np.array([a,b,c])
    result_mat = np.ones((3,3))
    mat = mat_maker2((3,3), *binom_x2y2(xpc,ypc), *binom_xy(xpc,ypc), *binom_x2y2(xpc,ypc,False))
    for i in range(mat.shape[0]):
        result_mat[i] = mat[i,:]*mult[i]
    
    print(f"""
    result mat:\n{result_mat}
    result mat sum: {result_mat.sum(axis=0)}
    result mat sum divided by denom: {result_mat.sum(axis=0)/denom}
    result mat sum divided by denom, -f: {result_mat.sum(axis=0)/denom/-f}
    """)
    return result_mat.sum(axis=0)/denom/-f

def rot_xy(phi,x,y,prime=True):
    '''prime=False implies that x,y coordinates represent those from
    standard xy-coordinate system; prime=True, implies x,y represent coordinates from
    x'y'-cooredinate system
    
    phi represents the angle formed between the x'-axis from
    the x'y'-coordiante system and the x-axis from the
    xy-coordiante system'''
    
    rads = np.deg2rad(phi)
    if not prime:        
        xc = (x*np.cos(rads)) + (y*np.sin(rads))
        yc = (-1*x*np.sin(rads)) + (y*np.cos(rads))
        return xc, yc
    else:
        xc = (x*np.cos(rads)) - (y*np.sin(rads))
        yc = (x*np.sin(rads)) + (y*np.cos(rads))
        return xc, yc


def rot_x(phi,x,y,prime=True):
    '''prime=False implies that x,y coordinates represent those from
    standard xy-coordinate system; prime=True, implies x,y represent coordinates from
    x'y'-cooredinate system
    
    phi represents the angle formed between the x'-axis from
    the x'y'-coordiante system and the x-axis from the
    xy-coordiante system'''
    
    rads = np.deg2rad(phi)
    if not prime:        
        xc = (x*np.cos(rads)) + (y*np.sin(rads))
        return xc
    else:
        xc = (x*np.cos(rads)) - (y*np.sin(rads))
        return xc

def rot_y(phi,x,y,prime=True):
    '''prime=False implies that x,y coordinates represent those from
    standard xy-coordinate system; prime=True, implies x,y represent coordinates from
    x'y'-cooredinate system
    
    phi represents the angle formed between the x'-axis from
    the x'y'-coordiante system and the x-axis from the
    xy-coordiante system'''
    
    rads = np.deg2rad(phi)
    if not prime:        
        yc = (-1*x*np.sin(rads)) + (y*np.cos(rads))
        return yc
    else:
        yc = (x*np.sin(rads)) + (y*np.cos(rads))
        return yc




def plot_rot(phi,x,y,prime=True):
    plt.plot(*rot_xy(phi,x,y,prime), linestyle='dashed')
    plt.plot(x,y)
    plt.show()
    return None

def plot_rot_noshow(phi,x,y,prime=True):
    plt.plot(*rot_xy(phi,x,y,prime), linestyle='dashed')
    # plt.plot(x,y)
    return None


def dx_rot(vertical,Dx,xlim):
    dxi = np.linspace(*xlim,100)
    dxc = eval_Dx(Dx) + 0*dxi
    
    if vertical:
        return (dxi,dxc)
    else:
        return (dxc,dxi)
    

def do_parabola_rot(phi,a,b,c,vertical=True, xlim=(-100,100), ylim=(-100,100)):
    hkp = get_hkp(a,b,c,vertical)
    vertex, focus, Dx, eq, direction = ret_VFDx(*hkp, vertical)
    print(f'vertex: V{vertex}')
    print(f'focus: F{focus}')
    xyvar = 'y' if vertical else 'x'
    print(f'Dx: {xyvar} = {eval_Dx(Dx)}')
    plotvars = get_plotvars(a,b,c,vertical,xlim)
    
    pvx,pvy = rot_xy(phi,*plotvars)
    dxx,dxy = rot_xy(phi,*dx_rot(vertical,Dx,xlim))
    

    
    plt.plot(pvx,pvy)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    # plt.hlines(eval_Dx(Dx), *xlim) if vertical else plt.vlines(eval_Dx(Dx), *ylim)
    plt.plot(dxx,dxy)
    plt.show()
    return None


def do_ellipse_rot(phi,asq,bsq,h=0,k=0):
    x, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = ellipse_plotvars(asq,bsq,h,k)
    print(f'''  
        xlim = {xlim}
        ylim = {ylim}
        majaxis = {majaxis}
        minaxis = {minaxis}
        foci = {foci}
        equation = {equation}''')
    
    xrott = rot_x(phi,xplot,ytop)
    xrotb = rot_x(phi,xplot,ybot)
    yrott = rot_y(phi,xplot,ytop)
    yrotb = rot_y(phi,xplot,ybot)
    hrot,krot = rot_xy(phi,h,k)
    

    plt.plot(xrott,yrott, c='r')
    plt.plot(xrotb,yrotb, c='r')
    plt.plot(hrot,krot, marker="o")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    # plt.plot(*foci[0],marker="o",c='c')
    # plt.plot(*foci[1],marker="o",c='c')
    # plt.plot(*majaxis[0],marker="o",c='m')
    # plt.plot(*majaxis[1],marker="o",c='m')
    # plt.plot(*minaxis[0],marker="o",c='y')
    # plt.plot(*minaxis[1],marker="o",c='y')

    plt.show()
    return None

def do_hyperbola_rot(phi,asq,bsq,h=0,k=0,horizontal=True,lab=False):
    asymptotes, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = hyperbola_plotvars(asq,bsq,h,k,horizontal)
    print(f'''  
        xlim = {xlim}
        ylim = {ylim}
        transverse axis = {majaxis}
        conjugate axis = {minaxis}
        foci = {foci}
        equation = {equation}
        asymptote equations: {asymptotes[2]}''')
        

    # xrott = rot_x(phi,xplot,ytop)
    # xrotb = rot_x(phi,xplot,ybot)
    # yrott = rot_y(phi,xplot,ytop)
    # yrotb = rot_y(phi,xplot,ybot)
    # hrot,krot = rot_xy(phi,h,k)
    # axpos,aypos = rot_xy(phi,*asymptotes[0])
    # axneg,ayneg = rot_xy(phi,*asymptotes[1])


    # if horizontal:
    #     plt.plot(yrott,xrott, c='r')
    #     plt.plot(yrotb,xrotb, c='r')
    #     # plt.plot(xplot,yrott, c='r')
    #     # plt.plot(xplot,ybot, c='r')
    #     # plt.plot(xrott,yrott, c='r')
    #     # plt.plot(xrotb,yrotb, c='r')

    # else:
    #     # plt.plot(yrott,xrott, c='r')
    #     # plt.plot(yrotb,xrotb, c='r')
    #     # plt.plot(yrott,xplot, c='r')
    #     # plt.plot(ybot,xplot, c='r')
    #     plt.plot(xrott,yrott, c='r')
    #     plt.plot(xrotb,yrotb, c='r')


    if horizontal:

        # xrott = rot_x(phi,xplot,ytop)
        # xrotb = rot_x(phi,xplot,ybot)
        # yrott = rot_y(phi,xplot,ytop)
        # yrotb = rot_y(phi,xplot,ybot)
        hrot,krot = rot_xy(phi,h,k)
        axpos,aypos = rot_xy(phi,*asymptotes[0])
        axneg,ayneg = rot_xy(phi,*asymptotes[1])
        # plt.plot(xrott,yrott, c='r')
        # plt.plot(xrotb,yrotb, c='r')


        yrott = rot_x(phi,ytop,xplot)
        xrott = rot_y(phi,ytop,xplot)
        yrotb = rot_x(phi,ybot,xplot)
        xrotb = rot_y(phi,ybot,xplot)
        plt.plot(yrott,xrott, c='r')
        plt.plot(yrotb,xrotb, c='r')
        # plt.plot(ytop,xplot, c='r')
        # plt.plot(ybot,xplot, c='r')
        # plt.plot(rot_xy(phi,xplot,ytop), c='r')
        # plt.plot(rot_xy(phi,xplot,ybot), c='r')
    
    else:
        xrott = rot_x(phi,xplot,ytop)
        xrotb = rot_x(phi,xplot,ybot)
        yrott = rot_y(phi,xplot,ytop)
        yrotb = rot_y(phi,xplot,ybot)
        hrot,krot = rot_xy(phi,h,k)
        axpos,aypos = rot_xy(phi,*asymptotes[0])
        axneg,ayneg = rot_xy(phi,*asymptotes[1])
        plt.plot(xrott,yrott, c='r')
        plt.plot(xrotb,yrotb, c='r')
        # plt.plot(ytop,xplot, c='r')
        # plt.plot(ybot,xplot, c='r')
        # plt.plot(rot_xy(phi,xplot,ytop), c='r')
        # plt.plot(rot_xy(phi,xplot,ybot), c='r')
        pass




    plt.plot(hrot,krot, marker="o")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    # plt.plot(*asymptotes[0], linestyle='dashed')
    # plt.plot(*asymptotes[1], linestyle='dashed')
    plt.plot(axpos,aypos, linestyle='dashed')
    plt.plot(axneg,ayneg, linestyle='dashed')
    plt.show()
    return None 

# f = -80
# denom = 100
# mult = np.array([18,-48,82])
# result_mat = np.ones((3,3))
# mat = mat_maker2((3,3), 90,-60,10, 30,80,-30, 10,60,90)
# for i in range(mat.shape[0]):
#     result_mat[i] = mat[i,:]*mult[i]
# print(f"""
#     result mat:\n{result_mat}
#     result mat sum: {result_mat.sum(axis=0)}
#     result mat sum divided by denom: {result_mat.sum(axis=0)/denom}
#     result mat sum divided by denom, -f: {result_mat.sum(axis=0)/denom/-f}
#     """)


# f = 45
# denom = 25
# mult = np.array([1,1,1])
# result_mat = np.ones((3,3))
# mat = mat_maker2((3,3), 5,-20,20, 40,-60,-40, 80,80,20)
# for i in range(mat.shape[0]):
#     result_mat[i] = mat[i,:]*mult[i]
# print(f"""
#     result mat:\n{result_mat}
#     result mat sum: {result_mat.sum(axis=0)}
#     result mat sum divided by denom: {result_mat.sum(axis=0)/denom}
#     result mat sum divided by denom, -f: {result_mat.sum(axis=0)/denom/-f}
#     """)


def do_hyperbola2(asq,bsq,h=0,k=0,horizontal=True,lab=False):
    asymptotes, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = hyperbola_plotvars(asq,bsq,h,k,horizontal)
    return (xplot, ytop, ybot)

# f = 0
# denom = 169
# mult = np.array([40,-36,25])
# result_mat = np.ones((3,3))
# mat = mat_maker2((3,3), 52,-156,117, 78,(-117+52),-78, 117,156,52)
# for i in range(mat.shape[0]):
#     result_mat[i] = mat[i,:]*mult[i]
# print(f"""
#     result mat:\n{result_mat}
#     result mat sum: {result_mat.sum(axis=0)}
#     result mat sum divided by denom: {result_mat.sum(axis=0)/denom}    
#     """)
# result mat sum divided by denom, -f: {result_mat.sum(axis=0)/denom/-f}

# f = 0
# denom = 289
# mult = np.array([64,-240,225])
# result_mat = np.ones((3,3))
# mat = mat_maker2((3,3), 225,-240,64, 120,(-64+225),-120, 64,240,225)
# for i in range(mat.shape[0]):
#     result_mat[i] = mat[i,:]*mult[i]
# print(f"""
#     result mat:\n{result_mat}
#     result mat sum: {result_mat.sum(axis=0)}
#     result mat sum divided by denom: {result_mat.sum(axis=0)/denom}    
#     """)
# result mat sum divided by denom, -f: {result_mat.sum(axis=0)/denom/-f}

def get_conic_type(a,b,c):
    val = (b**2) - (4*a*c)
    if val == 0:
        return 'parabola'
    elif val < 0:
        return 'ellipse'
    else: return 'hyperbola'
        