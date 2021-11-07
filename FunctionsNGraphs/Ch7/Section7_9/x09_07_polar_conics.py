from x09_06_polar_coords import *

def convert_polar_to_rect(r,theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

def distance(p1:tuple, p2:tuple):
    """
    need to convert polar coords to rectangular!
    
    then take the distance!
    """
    x1,y1 = convert_polar_to_rect(*p1)
    x2,y2 = convert_polar_to_rect(*p2)

    distance = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
    return distance

def get_majaxis_coords(majaxis_dict:dict):
    points = {}
    for i,k in enumerate(majaxis_dict):
        points[i] = (majaxis_dict[k], k)
    return points   

def polar_conic(_de, s, t, pos=True, cos=True, plot=False):
    """
    Let F be a fixed point and l a fixed line in a plane. The
    set of all points P in the plane such that the ratio d(P,F):
    d(P,Q) is a positive constant, e, where d(P,Q) is the 
    distance from P to l, is a conic section.  Moreover:

    if e == 1: parabola
    if e > 0, e < 1, ellipse
    if e > 1, hyperbola
    
    A polar equation that has one of the four forms:
    
    1. r = (d*e)/(1 + e*cos(theta)) # opens to the right
    2. r = (d*e)/(1 - e*cos(theta)) # opens to the left
    3. r = (d*e)/(1 + e*sin(theta)) # opens downward
    4. r = (d*e)/(1 - e*sin(theta)) # opens upward

    a generic form for these equations based on paramters for this function:
    r = _de/(s + sign*t*np.cos(theta) 

    
    rectangular form:

    (((x-h)**2)/(a**2)) + ((y**2)/(b**2)) = 1

    where:
    h = (-1*d*(e**2))/(1-(e**2)),
    a**2 = ((d**2)*(e**2))/((1-(e**2))**2)
    b**2 = ((d**2)*(e**2))/(1-(e**2))
    c**2 = ((d**2)*(e**4))/((1-(e**2))**2)
    c = (d*(e**2))/(1-(e**2))
    a = (d*e)/((1-(e**2)))
    b = (d*e)/((1-(e**2))**(1/2))
    e = c/a

    """
    # theta = np.linspace(0,2*pi, 1000)
    sign = 1 if pos else -1
    
    e = t/s
    if e == 1:
        type = 'parabola'
    elif 0 < e and e < 1:
        type = 'ellipse'
    else:
        type = 'hyperbola'
    

    if type == 'ellipse':
        majaxis = {}
        if cos:
            thetas = [0, pi]
            for theta in thetas:
                r = _de/(s + sign*t*np.cos(theta))
                majaxis[theta] = r
            
            points_dict = get_majaxis_coords(majaxis)
            x1,y1 = convert_polar_to_rect(*points_dict[0])
            x2,y2 = convert_polar_to_rect(*points_dict[1])
            dist = distance(points_dict[0],points_dict[1])
            a = dist/2
            c = a*e 
            b = ((a**2) - (c**2))**(1/2)
            asq = a**2
            bsq = b**2
            h = x1 + a if x1 < x2 else x1 - a

            if plot:
                do_ellipse(asq,bsq,h=h)
            

            print(f'''
            a = {a:>9.2f}
            b = {b:>9.2f}
            c = {c:>9.2f}
            e = {e:>9.2f}
            asq = {asq:>9.2f}
            bsq = {bsq:>9.2f}
            h = {h:>9.2f}
            ''')

            return a,b,c,e,asq,bsq,h

        
        else:
            thetas = [pi/2, (3*pi)/2]
            for theta in thetas:
                r = _de/(s + sign*t*np.sin(theta))
                majaxis[theta] = r

            points_dict = get_majaxis_coords(majaxis)
            x1,y1 = convert_polar_to_rect(*points_dict[0])
            x2,y2 = convert_polar_to_rect(*points_dict[1])
            dist = distance(points_dict[0],points_dict[1])
            a = dist/2
            c = a*e 
            b = ((a**2) - (c**2))**(1/2)
            asq = b**2
            bsq = a**2
            k = y1 + a if y1 < y2 else y1 - a

            if plot:
                do_ellipse(asq,bsq,k=k)
            
            print(f'''
            a = {a:>9.2f}
            b = {b:>9.2f}
            c = {c:>9.2f}
            e = {e:>9.2f}
            asq = {asq:>9.2f}
            bsq = {bsq:>9.2f}
            k = {k:>9.2f}
            ''')

            return a,b,c,e,asq,bsq,k

    if type == 'hyperbola':
        majaxis = {}
        if cos:
            thetas = [0, pi]
            for theta in thetas:
                r = _de/(s + sign*t*np.cos(theta))
                majaxis[theta] = r
            
            points_dict = get_majaxis_coords(majaxis)
            x1,y1 = convert_polar_to_rect(*points_dict[0])
            x2,y2 = convert_polar_to_rect(*points_dict[1])
            dist = distance(points_dict[0],points_dict[1])
            a = dist/2
            c = a*e 
            b = ((c**2) - (a**2))**(1/2)
            asq = a**2
            bsq = b**2
            h = x1 + a if x1 < x2 else x1 - a

            if plot:
                do_hyperbola(asq,bsq,h=h)
            

            print(f'''
            a = {a:>9.2f}
            b = {b:>9.2f}
            c = {c:>9.2f}
            e = {e:>9.2f}
            asq = {asq:>9.2f}
            bsq = {bsq:>9.2f}
            h = {h:>9.2f}
            ''')

            return a,b,c,e,asq,bsq,h

        
        else:
            thetas = [pi/2, (3*pi)/2]
            for theta in thetas:
                r = _de/(s + sign*t*np.sin(theta))
                majaxis[theta] = r

            points_dict = get_majaxis_coords(majaxis)
            x1,y1 = convert_polar_to_rect(*points_dict[0])
            x2,y2 = convert_polar_to_rect(*points_dict[1])
            dist = distance(points_dict[0],points_dict[1])
            a = dist/2
            c = a*e 
            b = ((c**2) - (a**2))**(1/2)
            asq = a**2
            bsq = b**2
            k = y1 + a if y1 < y2 else y1 - a

            if plot:
                do_hyperbola(asq,bsq,k=k,horizontal=False)
            
            print(f'''
            a = {a:>9.2f}
            b = {b:>9.2f}
            c = {c:>9.2f}
            e = {e:>9.2f}
            asq = {asq:>9.2f}
            bsq = {bsq:>9.2f}
            k = {k:>9.2f}
            ''')

            return a,b,c,e,asq,bsq,k