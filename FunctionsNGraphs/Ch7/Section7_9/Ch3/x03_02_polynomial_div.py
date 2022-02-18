from Ch3.x03_01_graph_polynomial import *

"""
DIVISION ALGORITHM FOR POLYNOMIALS


If f(x) and g(x) are polynomials, and if g(x) != 0, 
then there exist unique polynomials q(x) and r(x) such
that

    f(x) = g(x)*q(x) + r(x)

where either r(x) = 0 or the degree of r(x) is less than
the degree of g(x).

The polynomial q(x) is called the quotient and r(x) is
the remainder in the division of f(x) by g(x). 

"""

"""
so we have the coefficients of 2 polynomials, and
we want to perform polynomial division, so we want
sequentially eliminate the terms of our dividend in
decreasing order of degree, so we start with the
highest order term (degree=n), eliminate it, them 
move to eliminate term (degree=n-1), and so on until
the degree of the remainder polynomial is smaller 
than that of our divisor!

to eliminate the coefficients of the dividend 
polynomial, we find a real number that we can multiply
the coeffiecients of our our divisor by to produce
an intermediate polynomial, I'll call i(x), such
that when we add i(x) to the our dividend, we eliminate
the term (a_n*x**n) from the dividend.  this will
produce a new 'dividend', and a remainder.

so after each addition of our i(x) to the dividend,
we store 3 things: 

1. the multiplier, 
2. the updated dividend after adding the previous 
dividend to the i(x), and 
3. the resulting intermediate 'remainder' polynomial.

we check to see what the degree is of our intermediate
remainder polynomial, if it is less than that of our
divisor, we are done, otherwise, we continue and
repeat the previous step! 
    
"""

def get_degree(c):
    deg = len(c)-1
    return deg

def get_coeffs(c:dict):
    n = get_degree(c)
    coeffs = []
    for i in range(n,-1,-1):
        coeffs.append(c[f'a{i}'])
    return coeffs

def pad_coeffs(c1,c2):
    co1,co2=get_coeffs(c1), get_coeffs(c2)
    if len(co1) != len(co2):
        l1,l2=len(co1),len(co2)
        diff = abs(l1-l2)
        zeros = [int(x*0) for x in range(diff)]
        return zeros + co1
    return None

def get_mult(x,y):
    return x/y

def mult_coeffs(c:list, mult):
    return list(map(lambda x: x*mult, c))

def minus(x,y):
    return x-y

def add_poly(c1,c2):
    return list(map(minus,*zip(c1,c2)))

def lst_to_poly(lst):
    cee=dict()
    for i in range(len(lst)): 
        cee[f'a{i}'] = lst[len(lst)-1-i]
    return cee

def clst_expansion(lst,deg):
    llist=len(lst)
    if llist == deg + 1:
        return lst
    else:
        diff = abs((deg+1) - llist)
        for i in range(diff):
            lst.append(0)
        return lst
        
def poly_div(c1,c2,q=[]):
    """
    passing wrong type to pad_coeffs, but actually
    don't need pad_coeffs, instead, we need clst_expansion!
    or actually, instead of padding at the front, need
    to append 0 to the back of the list! 
    """
    d1,d2 = get_degree(c1), get_degree(c2)
    co1,co2 = get_coeffs(c1), get_coeffs(c2)
    mult=get_mult(co2[0],co1[0])
    q.append(mult)
    co1m=mult_coeffs(co1,mult)
    co1p=pad_coeffs(co1m,co2)
    rx = add_poly(co1p,co2)
    qx = clst_expansion(q,d2-d1)
    if get_degree(rx) < d1: 
        return qx,rx
    else:
        c2_ = lst_to_poly(rx)
        poly_div(c1,c2_,q)

if __name__ == '__main__':
    c1=gen_coeffs(1)
    c2=gen_coeffs(4)
    qx,rx = poly_div(c1,c2)
    print(f'qx:{qx}, rx:{rx}')