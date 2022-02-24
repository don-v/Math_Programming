from Ch3.x03_01_graph_polynomial import *
import re

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
that when we subtract i(x) to the our dividend, we 
eliminate the term (a_n*x**n) from the dividend.  this 
will produce a new 'dividend', and a remainder.

so after each subtraction of our updated i(x) from 
the dividend, we store 3 things: 

1. the multiplier, 
2. the updated dividend after adding the previous 
dividend to the i(x), and 
3. the resulting intermediate 'remainder' polynomial.

we check to see what the degree is of our intermediate
remainder polynomial, if it is less than that of our
divisor, we are done, otherwise, we continue and
repeat the previous steps! 
    
"""

def get_degree(c):
    """returns the degree of a polynomial specified
    using either a list of coefficients, or a dict of
    coefficients"""

    deg = len(c)-1
    return deg

def get_coeffs(c:dict):
    """extracts the coefficients of a polynomial specified
    as a dict and returns a list of the coefficinets, ordered
    from [n, n-1, ..., 0], where n represetns the degree
    of the polynomial term"""

    n = get_degree(c)
    coeffs = []
    for i in range(n,-1,-1):
        coeffs.append(c[f'a{i}'])
    return coeffs

def pad_coeffs(c1,c2):
    """c1 and c2 represent lists of coefficients of 
    different lengths, but that represetns polynomials
    of identical degree, and in order for corresponding 
    elements of them to be added, zeros are added to the 
    end of the shorter list of coefficients """

    co1,co2=c1,c2
    if len(co1) != len(co2):
        l1,l2=len(co1),len(co2)
        diff = abs(l1-l2)
        zeros = [int(x*0) for x in range(diff)]
        return co1 + zeros
    return co1

def get_mult(x,y):
    """returns the factor by which the divisor is multiplied
    such that when the the product of the divisor and multiplier
    is substracted from the dividend, the highest order term of
    the dividend is eliminated"""

    return x/y

def mult_coeffs(c:list, mult):
    """function used to multiply every element of a list
    by a constant factor, 'mult'"""

    return list(map(lambda x: x*mult, c))

def minus(tup):
    """returns the result of subtracting the 2nd term of
    a tuple from the 1st term"""

    return tup[0]-tup[1]

def sub_poly(c1,c2):
    """returns the result of subtracting corresponding
    elements of lists of the same length. the corresponding 
    elements of c2 are subtracted from c1"""

    return list(map(minus,zip(c1,c2)))

def lst_to_poly(lst):
    """converts a list of polynomial coefficients ordered
    in decreasing polynomial term degree with increasing 
    list index to a dict of coefficients that has its keys indexed
    from a0 to an"""

    cee=dict()
    for i in range(len(lst)): 
        cee[f'a{i}'] = lst[len(lst)-1-i]
    return cee

def clst_expansion(lst,deg):
    """given a list of coefficients that should correspond
    to a specified polynomial degree, zeros are added to the
    list at the end of the list to match the length of a list
    of polynomial specified polynomial degree.
    
    for example, if a list of polynomial coefficients is to
    represent a polynomial of degree 3, it should have a length
    of 4, so if this function is presented with a polynomial
    cofficient list of length 1, and it should be length 4, 3
    zeros are appened to the end of the list"""

    llist=len(lst)
    if llist == deg + 1:
        return lst
    else:
        diff = abs((deg+1) - llist)
        for i in range(diff):
            lst.append(0)
        return lst
        
def poly_div(c1,c2,q=[],n=0):
    """
    a recursive function that carries out polynomial division,
    where c1 represents the divisor, and c2 the dividend, and
    returns the quotient and remainder of the division
    """
    d1,d2 = get_degree(c1), get_degree(c2)
    co1,co2 = get_coeffs(c1), get_coeffs(c2)
    if d2 < d1:
        return 0,co2
    mult=get_mult(co2[0],co1[0])
    q.append(mult)
    co1m=mult_coeffs(co1,mult)
    co1p=pad_coeffs(co1m,co2)
    rx = sub_poly(co2,co1p)[1:]
    qx = clst_expansion(q[:],d2+n-d1)
    if get_degree(rx) < d1:
        return qx,rx
    else:
        n +=1
        c2_ = lst_to_poly(rx)
        return poly_div(c1,c2_,q,n)

def poly_display_from_list(x):
    """if x is a list of polynomial coefficients, ordered
    in decreasing polynomial degree with increasing list 
    index then it returns a string representation of a polynomial,
    otherwise, it returns x"""
    if isinstance(x,list):
        coeff_dict=lst_to_poly(x)
        degree=get_degree(x)
        return poly_display(coeff_dict,degree)
    else:
        return x

def eval_remainder_at_x(r,x):
    '''evaluate the remainder polynomial at x. note:
    the remainder polynomial is of degree 0, when we have
    divisor of degree 1: x-c, for some real constant c'''
    remainder_coeffs_dict = lst_to_poly(r)
    remainder_degree=get_degree(r)
    remainder_poly = poly_display(remainder_coeffs_dict,remainder_degree)
    remainder_eval_at_x=eval_poly2(x,remainder_poly)
    return remainder_eval_at_x

def remainder_theorem(coeff_list, x):
    '''Remainder Theorem: If a polynomial f(x) is divided by x-c, 
    then the remainder, r(x), is f(c)'''
    factor = [1,-x]
    divisor,dividend = lst_to_poly(factor), lst_to_poly(coeff_list)
    q,r = poly_div(divisor,dividend)
    degree = get_degree(dividend)
    poly = poly_display(dividend,degree)
    f_at_x = eval_poly2(x,poly)
    remainder_eval_at_x=eval_remainder_at_x(r,x)
    print(f'''{'*'*len('remainder from polynomial division:')}
    remainder from polynomial division:
    {r}
    evaluating polynomial at c:
    {f_at_x}
    does the remainder polynomial equal the value of the function at c?
    {'Yes it does!' if remainder_eval_at_x==f_at_x else "No, No it doesn't!"}''')
    
    return r, f_at_x

def eval_poly3(coeff_list):
    ['x**{}'.format(x) for x in range(3,-1,-1)]
    pass

if __name__ == '__main__':
    c1=[1,-4]
    c2=[2,-1,-5,3]
    divisor = lst_to_poly(c1)
    dividend = lst_to_poly(c2)
    q,r = poly_div(divisor,dividend)
    print(f'q:{poly_display_from_list(q)}; r:{poly_display_from_list(r)}')