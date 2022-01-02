from x09_03_ellipses import *
from math import sqrt


def display_sign(x):
    if x < 0:
        sign = f'+{abs(x)}'
    elif x == 0:
        sign = ''
    else:
        sign = f'-{abs(x)}'
    return sign

def ret_hyperbola_plotrng(factor,a,b, h,k):
    use = a if a>b else b
    val = 2*use*(factor+1)
    xlim = ((-val+h),(val+h))
    ylim = ((-val+k),(val+k))
    return (xlim,ylim)

def hyperbola_plotvars(asq,bsq,h=0,k=0,horizontal=True):
    '''
    ****************************************************
    hyperbola with major axis along x-axis:
    
    (x^2/a^2) - (y^2/b^2) = 1
    
    with vertices (+/-a,0). 
    
    The foci are (+/-c,0), where c^2=a^2+b^2

    asymptotes: y = +/-(b/a)*x

    ****************************************************
    ****************************************************
    hyperbola with major axis along y-axis:

    (y^2/a^2) - (x^2/b^2) = 1

    with vertices (0,+/-a). 
    
    The foci are (0,+/-c), where c^2=a^2+b^2

    asymptotes: y = +/-(a/b)*x
    ****************************************************
    '''
    a = asq**(1/2)
    b = bsq**(1/2)
    c = (asq+bsq)**(1/2)
    if horizontal:
        # y = np.linspace((-1.5*a),(1.5*a),1000)
        y = np.linspace((-1*(1.5*(b+a))),(1.5*(b+a)),1000)
        xplot = y + k
        ytop = ((a/b)*(((y**2)+(b**2))**(1/2)))+h
        ybot = -ytop + (2*h)
        # x = np.linspace((-1.5*a),(1.5*a),1000)
        # xplot = x + h
        # ytop = ((b/a)*(((x**2)-(a**2))**(1/2)))+k
        # ybot = -ytop + (2*k)
        xlim = ret_hyperbola_plotrng(0.2,a,b,h,k)[0]
        ylim = ret_hyperbola_plotrng(0.2,a,b,h,k)[1]
        asympx = np.linspace(*xlim,100) 
        asympypos = ((b/a)*(asympx-h)) + k
        asympyneg = (-1*(asympypos-k))+k
        asymptotes_lines = f'''
        y{display_sign(k)} = {b/a}*(x{display_sign(h)})
        y{display_sign(k)} = {-1*(b/a)}*(x{display_sign(h)})'''
        asymptotes = (asympx,asympypos),(asympx,asympyneg), asymptotes_lines
        majaxis = (a+h,k),(-a+h,k)
        maj_display = f'({a+h:.2f},{k}),({-a+h:.2f},{k})'
        minaxis = (h,b+k), (h,-b+k)
        min_display = f'({h},{b+k:.2f}),({h},{-b+k:.2f})'
        foci = (c+h,k), (-c+h,k)
        foci_display = f'({c+h:.2f},{k}), ({-c+h:.2f},{k})'
        equation = f'''((x{display_sign(h)})**2)/{asq} - ((y{display_sign(k)})**2)/{bsq} = 1'''
    
    else:
        # y = np.linspace((-1.5*a),(1.5*a),1000)
        # xplot = y + k
        # ytop = ((b/a)*(((y**2)-(a**2))**(1/2)))+h
        # ybot = -ytop + (2*h)
        x = np.linspace((-1.5*(b+a)),(1.5*(b+a)),1000)
        xplot = x + h
        ytop = ((a/b)*(((x**2)+(b**2))**(1/2)))+k
        ybot = -ytop + (2*k)
        xlim = ret_hyperbola_plotrng(0.2,a,b,h,k)[0]
        ylim = ret_hyperbola_plotrng(0.2,a,b,h,k)[1]
        asympx = np.linspace(*xlim,100)
        asympypos = ((a/b)*(asympx-h)) + k
        asympyneg = (-1*(asympypos-k))+k
        asymptotes_lines = f'''
        y{display_sign(k)} = {a/b}*(x{display_sign(h)})
        y{display_sign(k)} = {-1*(a/b)}*(x{display_sign(h)})'''
        asymptotes = (asympx,asympypos),(asympx,asympyneg), asymptotes_lines
        majaxis = (h,-a+k), (h,a+k)
        maj_display = f'({h},{-a+k:.2f}), ({h},{a+k:.2f})'
        minaxis = (b+h,k), (-b+h,k)
        min_display = f'({b+h:.2f},{k}), ({-b+h:.2f},{k})'
        foci = (h,-c+k), (h,c+k)
        foci_display = f'({h},{-c+k:.2f}), ({h},{c+k:.2f})'
        equation = f'''((y{display_sign(k)})**2)/{asq} - ((x{display_sign(h)})**2)/{bsq} = 1'''
    
    return (asymptotes, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation)

    
def do_hyperbola(asq,bsq,h=0,k=0,horizontal=True,lab=False):
    asymptotes, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = hyperbola_plotvars(asq,bsq,h,k,horizontal)
    print(f'''  
        xlim = {xlim}
        ylim = {ylim}
        transverse axis = {majaxis}
        conjugate axis = {minaxis}
        foci = {foci}
        equation = {equation}
        asymptote equations: {asymptotes[2]}''')
        
    
    if horizontal:
        plt.plot(ytop,xplot, c='r')
        plt.plot(ybot,xplot, c='r')
        # plt.plot(xplot,ytop, c='r')
        # plt.plot(xplot,ybot, c='r')
    
    else:
        # plt.plot(ytop,xplot, c='r')
        # plt.plot(ybot,xplot, c='r')
        plt.plot(xplot,ytop, c='r')
        plt.plot(xplot,ybot, c='r')
    
    plt.plot(h,k, marker="o")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.plot(*asymptotes[0], linestyle='dashed')
    plt.plot(*asymptotes[1], linestyle='dashed')
    plt.plot(*foci[0],marker="o",c='c')
    plt.plot(*foci[1],marker="o",c='c')
    plt.plot(*majaxis[0],marker="o",c='m')
    plt.plot(*majaxis[1],marker="o",c='m')
    plt.plot(*minaxis[0],marker="o",c='y')
    plt.plot(*minaxis[1],marker="o",c='y')
    

    if lab:
        plt.annotate(
            f'Foci: {foci_display}', 
            foci[0],
            xycoords='data',
                    xytext=(.5,1), textcoords='axes fraction',
                    size=20, va="center", ha="center",
                    bbox=dict(boxstyle="round4", fc="w"),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.2",
                                    fc="w"),
            )
        
        plt.annotate(
            '', 
            foci[1],
            xycoords='data',
                    xytext=(.5,1), textcoords='axes fraction',
                    size=20, va="center", ha="center",
                    #   bbox=dict(boxstyle="round4", fc="w"),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.2",
                                    fc="w"),
            )

    # *****************************************************************


        plt.annotate(
            f'Major axis: {maj_display}', 
            majaxis[0],
            xycoords='data',
                    xytext=(0.75,-0.1), textcoords='axes fraction',
                    size=20, va="center", ha="center",
                    bbox=dict(boxstyle="round4", fc="w"),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.2",
                                    fc="w"),
            )
        
        plt.annotate(
            '', 
            majaxis[1],
            xycoords='data',
                    xytext=(0.75,-0.1), textcoords='axes fraction',
                    size=20, va="center", ha="center",
                    #   bbox=dict(boxstyle="round4", fc="w"),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.2",
                                    fc="w"),
            )


    # *****************************************************************

        plt.annotate(
            f'Minor axis: {min_display}', 
            minaxis[0],
            xycoords='data',
                    xytext=(0.25,-0.1), textcoords='axes fraction',
                    size=20, va="center", ha="center",
                    bbox=dict(boxstyle="round4", fc="w"),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.2",
                                    fc="w"),
            )
        
        plt.annotate(
            '', 
            minaxis[1],
            xycoords='data',
                    xytext=(0.25,-0.1), textcoords='axes fraction',
                    size=20, va="center", ha="center",
                    #   bbox=dict(boxstyle="round4", fc="w"),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.2",
                                    fc="w"),
            )


    plt.show()


def track_negative_ab(asq, bsq):
    return (True if asq > 0 else False)


def expanded_hyperbola(a,c,d,e,f):
    h = -1*(d/(2*a))
    k = -1*(e/(2*c))

    const = (-f) + ((d**2)/(4*a)) + ((e**2)/(4*c))
    asq = const/a
    bsq = const/c
    horizontal = track_negative_ab(asq,bsq)

    if horizontal:
        return abs(asq),abs(bsq),h,k,horizontal
    else:
        return abs(bsq),abs(asq),h,k,horizontal


def plot_prep(x,y):
    plt.plot(x,y)
    plt.plot(y,x)
    return None 



def do_hyperbola_noshow(asq,bsq,h=0,k=0,horizontal=True,lab=False):
    asymptotes, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = hyperbola_plotvars(asq,bsq,h,k,horizontal)
    print(f'''  
        xlim = {xlim}
        ylim = {ylim}
        transverse axis = {majaxis}
        conjugate axis = {minaxis}
        foci = {foci}
        equation = {equation}
        asymptote equations: {asymptotes[2]}''')
        
    
    if horizontal:
        plt.plot(ytop,xplot, c='r')
        plt.plot(ybot,xplot, c='r')
        # plt.plot(xplot,ytop, c='r')
        # plt.plot(xplot,ybot, c='r')
    
    else:
        # plt.plot(ytop,xplot, c='r')
        # plt.plot(ybot,xplot, c='r')
        plt.plot(xplot,ytop, c='r')
        plt.plot(xplot,ybot, c='r')
    
    plt.plot(h,k, marker="o")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.plot(*asymptotes[0], linestyle='dashed')
    plt.plot(*asymptotes[1], linestyle='dashed')
    plt.plot(*foci[0],marker="o",c='c')
    plt.plot(*foci[1],marker="o",c='c')
    plt.plot(*majaxis[0],marker="o",c='m')
    plt.plot(*majaxis[1],marker="o",c='m')
    plt.plot(*minaxis[0],marker="o",c='y')
    plt.plot(*minaxis[1],marker="o",c='y')
    return None 


def display_sign_pos(x):
    if x < 0:
        sign = f'-{abs(x)}'
    elif x == 0:
        sign = ''
    else:
        sign = f'+{abs(x)}'
    return sign


def plot_line(a,b,c):
    slope = -a/b
    intercept = -c/b
    x = np.linspace((-1*abs(intercept))-10, abs(intercept)+10, 1000)
    y = (slope*x) + intercept
    eq_std = f'''{a}*x{display_sign_pos(b)}*y{display_sign_pos(c)} = 0'''
    eq_mxb = f'''y = {slope}*x{display_sign_pos(intercept)}'''
    print(f"""
    Equations:
    standard form : 
    {eq_std}
    slope-intercept form: 
    {eq_mxb}
    """)
    plt.plot(x,y)
    return slope, intercept, eq_std, eq_mxb


def study_eccentricity_h(a,b=0.01):
    while b < a:
        asq = a**2
        bsq = b**2
        eccentricity = (asq-bsq)**(1/2)
        do_hyperbola_noshow(asq,bsq)
        print(f'eccentricity={eccentricity}')
        b += .2
    return None 