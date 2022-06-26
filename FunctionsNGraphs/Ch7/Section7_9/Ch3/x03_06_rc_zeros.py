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

def get_abs_value(x):
    if x >= 0:
        return x
    else:
        return -x

def get_factors(x):
    """returns factors of x"""
    facts = list()        
    for i in range(1,x+1):
        if x % i == 0:
            facts.append(i)
    return facts
 

def get_possible_zeros(a_n,a_0):
    possible_c = get_factors(get_abs_value(a_0))
    possible_d_pos = get_factors(a_n)
    possible_d = list(map(lambda j: j*-1, possible_d_pos)) + possible_d_pos
    positive_possibles = product(possible_c,possible_d)
    possible_zeros = list()
    for c,d in positive_possibles:
        possible_zeros.append(f'{c}/{d}')
    return possible_zeros

# def recursive_syn_div(zero, coeffs, possible_zeros, confirmed_zeros = []):
#     while get_degree(coeffs) >2:
#         for zero in possible_zeros:
#             qr = synthetic_division(zero, coeffs)
#             if get_abs_value(qr[-1]) < 0.001:
#                 confirmed_zeros.append(zero)
#                 coeffs = qr[:-1]

def complex_roots_(a,b,c):
    d=((math.pow(b,2))-(4*a*c))
    if a!=0:
        if d>0:
           x1=(-b+math.sqrt(d))/(2*a)
           x2=(-b-math.sqrt(d))/(2*a)
           print("x1=",x1," and x2=",x2)
           print("real root")
           return x1,x2
        elif d==0:
           x=-b/(2*a)
           print("x=",x)
           print("equal root" )
           return (x1,)
        elif d<0:
            x1=(-b+cmath.sqrt(d))/(2*a)
            x2=(-b-cmath.sqrt(d))/(2*a)
            print("x1=",x1," and x2=",x2)
            print("complex root")
            return x1,x2
    else:
        print("this is not quadratic equation")

def get_rational_zeros(coeffs:list):
    an,a0 = coeffs[0],coeffs[-1]
    possible_zeros = get_possible_zeros(an,a0)
    confirmed_zeros = list()
    for zero in possible_zeros.copy():
        qr = synthetic_division(eval(zero), coeffs)
        r = qr[-1]
        if get_abs_value(r) < .001:
            confirmed_zeros.append(zero)
            coeffs = qr[:-1]
            if get_degree(coeffs) == 2:
                zeros = complex_roots_(*coeffs)
                for z in zeros:
                    confirmed_zeros.append(z)
                break
        else: 
            continue
    return confirmed_zeros

def get_list(x):
    z = list()
    while len(z) < x:
        num = input('enter a number to add to the list: ')
        z.append(int(num))
    return z

if __name__ == '__main__':
    coeffs = [1,-1,-10,-8]
    possible_zeros = get_possible_zeros(1,-8)
    # possible_zeros = list(map(str,list(range(-5,6))))
    confirmed_zeros = list()
    for zero in possible_zeros.copy():
        qr = synthetic_division(eval(zero), coeffs)
        r = qr[-1]
        if get_abs_value(r) < .001:
            confirmed_zeros.append(zero)
            coeffs = qr[:-1]
            if get_degree(coeffs) == 2:
                zeros = complex_roots_(*coeffs)
                for z in zeros:
                    confirmed_zeros.append(z)
                break
        else: 
            continue
    print(confirmed_zeros)



    # while get_degree(coeffs) >2:
    #     for zero in possible_zeros:
    #         qr = synthetic_division(zero, coeffs)
    #         if get_abs_value(qr[-1]) < 0.001:
    #             confirmed_zeros.append(zero)
    #             coeffs = qr[:-1]
                
    
