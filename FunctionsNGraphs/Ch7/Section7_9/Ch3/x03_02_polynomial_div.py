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

def get_degree(c:dict):
    deg = len(c.keys())-1
    return deg

def get_coeffs(c:dict):
    n = get_degree(c)
    coeffs = []
    for i in range(n,-1,-1):
        coeffs.append(c[f'a{i}'])
    return coeffs

def pad_coeffs(c1,c2):
    if len(c1) != len(c2):
        l1,l2=len(c1),len(c2)
        diff = l1-l2
        zeros = [int(x*0) for x in range(diff)]
        return zeros + c1
    return None

def get_mult(x,y):
    return -x/y

def mult_coeffs(c:list, mult):
    return map(lambda x: x*mult, c)

def add_poly(c1,c2):
    return map(sum,zip(c1,c2))

def lst_to_poly(lst):
    pass

if __name__ == '__main__':
    c = gen_coeffs(3)
    degree = get_degree(c)
    coeffs = get_coeffs(c)
    p = poly_display(c,degree)
    print(p)
    print('the degree is:',degree)
    print('the coeffs are:', coeffs)