from x09_06_polar_coords import *

def polar_conic(_de, sign='pos', cos=True):
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