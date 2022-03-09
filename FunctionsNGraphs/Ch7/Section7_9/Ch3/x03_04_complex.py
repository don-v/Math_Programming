from Ch3.x03_03_synthetic_div import *
import math, cmath
from x09_09_review import *

def add_complex(z1,z2):
    """adds two complex numbers where z1 and z2
    are of the form a + bi, where 'a' and 'b' 
    are real numbers and i is defined such that 
    i**2 = -1"""
    return z1 + z2

def sub_complex(z1,z2):
    """returns difference of two complex numbers 
    where z1 and z2 are of the form a + bi, where 
    'a' and 'b' are real numbers and i is defined 
    such that i**2 = -1"""
    return z1 - z2

def mult_complex(z1,z2):
    """returns the prooduct of two complex numbers,
    z1 and z2, where z1 and z2 are of the form 
    `a + bi`, where 'a' and 'b' are real numbers 
    and i is defined such that i**2 = -1"""
    return z1*z2

def gen_complex():
    """prompts user to enter the values of 
    a and be to contruct a complex number of
    the form `a + bi`, where 'a' and 'b' are 
    real numbers and i is defined such that 
    i**2 = -1"""
    a = int(input('what is the value of a? '))
    b = int(input('what is the value of b? '))
    return complex(a,b)

def gen_n_complex(n=2):
    """generate and return two complex numbers
    of the form `a + bi`, where 'a' and 'b' are 
    real numbers and i is defined such that 
    i**2 = -1"""
    cnums = list()
    for i in range(n):
        print(f'get a and b for z{i+1}:')
        cnums.append(gen_complex())
    return cnums[0], cnums[1]

def simplify_complex_fraction(numerator, denominator):
    """converting a fraction in which the numerator and
    denominator are represented by complex numbers to a
    singular complex number of the form `a + bi`, where 
    'a' and 'b' are real numbers and i is defined such 
    that i**2 = -1"""
    d_conjugate = denominator.conjugate()
    complex_const = denominator*d_conjugate
    const = complex_const.real
    result = numerator*d_conjugate

    s = f"""
    
        {result.real}                      {result.imag}       
    -------------    +    -------------  i
        {const}                     {const}"""

    return (1/const)*result, s


def complex_roots():
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    c=int(input("enter c: "))
    d=((math.pow(b,2))-(4*a*c))
    if a!=0:
        if d>0:
           x1=(-b+math.sqrt(d))/(2*a)
           x2=(-b-math.sqrt(d))/(2*a)
           print("x1=",x1," and x2=",x2)
           print("real root")
        elif d==0:
           x=-b/(2*a)
           print("x=",x)
           print("equal root" )
        elif d<0:
            x1=(-b+cmath.sqrt(d))/(2*a)
            x2=(-b-cmath.sqrt(d))/(2*a)
            print("x1=",x1," and x2=",x2)
            print("complex root")
    else:
        print("this is not quadratic equation")

def csqrt(x):
    """returns the square root of a real number in
    complex form; can handle the case of a real number
    less than 0!"""
    if x < 0:
        return complex(0,math.sqrt(-x))
    else: return complex(math.sqrt(x),0)


if __name__ == '__main__':
    z1,z2 = gen_n_complex()
    print(f'z1: {z1}')
    print(f'z2: {z2}')
    print(f'sum z1 + z2: {add_complex(z1,z2)}')
    print(f'difference z1 - z2: {sub_complex(z1,z2)}')
    print(f'product z1 * z2: {mult_complex(z1,z2)}')
    f,s = simplify_complex_fraction(z1,z2)
    print(f"""
    fraction:
    
        {z1}
    -------------
        {z2}

    simplified: 
    
    {s}""")
    
    
