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

def get_degree(c:dict):
    deg = len(c.keys())-1
    return deg

def get_coeffs(c:dict):
    n = get_degree(c)
    coeffs = []
    for i in range(n,-1,-1):
        coeffs.append(c[f'a{i}'])
    return coeffs

def elim_coeff(c1,c2):
    d1,d2 = get_degree(c1), get_degree(c2)
    co1,co2 = get_coeffs(c1), get_coeffs(c2)
    return (d1,d2),(co1,co2)

if __name__ == '__main__':
    c = gen_coeffs(3)
    degree = get_degree(c)
    coeffs = get_coeffs(c)
    p = poly_display(c,degree)
    print(p)
    print('the degree is:',degree)
    print('the coeffs are:', coeffs)