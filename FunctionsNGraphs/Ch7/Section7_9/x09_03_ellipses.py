from x09_02_parabolas import *

def display_sign(x):
    if x < 0:
        sign = f'+{abs(x)}'
    elif x == 0:
        sign = ''
    else:
        sign = f'-{abs(x)}'
    return sign

def ret_ellipse_plotrng(factor,a,b, h,k):
    use = a if a>b else b
    val = 2*use*(factor+1)
    xlim = ((-val+h),(val+h))
    ylim = ((-val+k),(val+k))
    return (xlim,ylim)

def ellipse_plotvars(asq,bsq,h=0,k=0):
    '''
    ****************************************************
    Ellipse with major axis along x-axis:
    
    (x^2/a^2) + (y^2/b^2) = 1
    
    for a^2 > b^2, is an ellipse with vertices (+/-a,0). 
    The endpoints of the minor axis are (0,+/-b).

    The foci are (+/-c,0), where c^2=a^2-b^2

    ****************************************************
    ****************************************************
    Ellipse with major axis along y-axis:

    (x^2/b^2) + (y^2/a^2) = 1

    for a^2 > b^2, is an ellipse with vertices (0,+/-a). 
    The endpoints of the minor axis are (+/-b,0).

    The foci are (0,+/-c), where c^2=a^2-b^2
    ****************************************************
    '''
    horizontal = True if asq>bsq else False
    a = asq**(1/2)
    b = bsq**(1/2)
    if horizontal:
        use = asq-bsq
        c = use**(1/2)
        majaxis = (a+h,k),(-a+h,k)
        maj_display = f'({a+h:.2f},{k}),({-a+h:.2f},{k})'
        minaxis = (h,b+k), (h,-b+k)
        min_display = f'({h},{b+k:.2f}),({h},{-b+k:.2f})'
        foci = (c+h,k), (-c+h,k)
        foci_display = f'({c+h:.2f},{k}), ({-c+h:.2f},{k})'
    
    else:
        use = bsq-asq
        c = use**(1/2)
        majaxis = (h,b+k),(h,-b+k)
        maj_display = f'({h},{b+k:.2f}),({h},{-b+k:.2f})'
        minaxis = (a+h,k), (-a+h,k)
        min_display = f'({a+h:.2f},{k}),({-a+h:.2f},{k})'
        foci = (h,c+k), (h,-c+k)
        foci_display = f'({h},{c+k:.2f}), ({h},{-c+k:.2f})'
    x = np.arange(-a,a+.001,.001)
    xplot = x + h
    ytop = ((b/a)*(((a**2)-(x**2))**(1/2)))+k
    ybot = -ytop + (2*k)
    xlim = ret_ellipse_plotrng(0.2,a,b,h,k)[0]
    ylim = ret_ellipse_plotrng(0.2,a,b,h,k)[1]
    
    
    equation = f'''((x{display_sign(h)})**2)/{asq} + ((y{display_sign(k)})**2)/{bsq} = 1'''
    return (x, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation)

    
def do_ellipse(asq,bsq,h=0,k=0):
    x, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = ellipse_plotvars(asq,bsq,h,k)
    print(f'''  
        xlim = {xlim}
        ylim = {ylim}
        majaxis = {majaxis}
        minaxis = {minaxis}
        foci = {foci}
        equation = {equation}''')
    
    
    plt.plot(xplot,ytop, c='r')
    plt.plot(xplot,ybot, c='r')
    plt.plot(h,k, marker="o")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.plot(*foci[0],marker="o",c='c')
    plt.plot(*foci[1],marker="o",c='c')
    plt.plot(*majaxis[0],marker="o",c='m')
    plt.plot(*majaxis[1],marker="o",c='m')
    plt.plot(*minaxis[0],marker="o",c='y')
    plt.plot(*minaxis[1],marker="o",c='y')
    


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


def expanded_ellipse(a,c,d,e,f):
    h = -1*(d/(2*a))
    k = -1*(e/(2*c))

    const = (-f) + ((d**2)/(4*a)) + ((e**2)/(4*c))
    asq = const/a
    bsq = const/c

    return asq,bsq,h,k


def plot_prep(x,y):
    plt.plot(x,y)
    plt.plot(y,x)
    return None 



def do_ellipse_noshow(asq,bsq,h=0,k=0):
    x, xplot, ytop, ybot, xlim, ylim, majaxis, maj_display, minaxis, min_display, foci, foci_display, equation = ellipse_plotvars(asq,bsq,h,k)
    print(f'''  
        xlim = {xlim}
        ylim = {ylim}
        majaxis = {majaxis}
        minaxis = {minaxis}
        foci = {foci}
        equation = {equation}''')


    plt.plot(xplot,ytop, c='r')
    plt.plot(xplot,ybot, c='r')
    plt.plot(h,k, marker="o")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.hlines(0, *xlim, 'k')
    plt.vlines(0, *ylim, 'k')
    plt.plot(*foci[0],marker="o",c='c')
    plt.plot(*foci[1],marker="o",c='c')
    plt.plot(*majaxis[0],marker="o",c='m')
    plt.plot(*majaxis[1],marker="o",c='m')
    plt.plot(*minaxis[0],marker="o",c='y')
    plt.plot(*minaxis[1],marker="o",c='y')
    return None 


def study_eccentricity(a,b=0.01):
    while b < a:
        asq = a**2
        bsq = b**2
        eccentricity = (asq-bsq)**(1/2)
        do_ellipse_noshow(asq,bsq)
        print(f'eccentricity={eccentricity}')
        b += .2
    return None 