from Ch3.x03_05_poly_zeros import *
from itertools import product

"""
Theorem: If f(x) is a polynomial of degree n > 0
and has real coefficients and if z is a complex
zero of f(x), then the conjugate z-bar of z is
also a zero of f(x)
"""

"""
Theorem: Every polynomial with real coefficients and 
positive degree n can be expressed as a product of 
linear and quadratic polynomials with real coefficients 
where the quadractic factors have no real zeros
"""

"""
Theorem of Rational Zeros: Suppose that 
f(x) = a_n*x**n + a_{n-1}*x**(n-1) + ...
+ a_1*x**1 + a_0 is a polynomial with
integer coeffcients. If c/d is a rational
zero of f(x), where c and d have no common
prime factors and c > 0, then c is a factor
of a_0 and d is a factor of a_n.
"""

def get_factors(x):
    """returns factors of x"""
    facts = list()        
    for i in range(1,x+1):
        if x % i == 0:
            facts.append(i)
    return facts
 

def get_possible_zeros(a_0,a_n):
    possible_c = get_factors(a_0)
    possible_d_pos = get_factors(a_n)
    possible_d = list(map(lambda j: j*-1, possible_d_pos)) + possible_d_pos
    positive_possibles = product(possible_c,possible_d)



if __name__ == '__main__':
    pass
