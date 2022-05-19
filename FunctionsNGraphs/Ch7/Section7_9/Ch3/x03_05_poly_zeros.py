from Ch3.x03_04_complex import *
from itertools import product

def is_pos(x):
    """returns a boolean value for testing if x is positive"""
    return x > 0

def get_two(x,n=2):
    """returns successive slices of a list of size n"""
    doubles = list()
    if len(x) < 2:
        return x
    else:
        i = 0
        while i < len(x)-1:
            n_slice = x[i:i+n]
            doubles.append((n_slice[0],n_slice[1]))
            i += 1
    return doubles

def check_tuple_sign_change(x:tuple):
    """compares the signs of a 2-tuple, and returns
    True if the signs are different, otherwise, returns
    False, all 2-tuple elements must be non-zero"""
    if is_pos(x[0]) == is_pos(x[1]):
        return False
    return True

def get_descarte_signs(x: list) -> int:
    """takes non-zero coefficients of a polynomial 2
    at a time and determines if there is a sign change
    between the two coefficients"""
    sign_changes = 0
    doubles = get_two(x)
    for double in doubles:
        if check_tuple_sign_change(double):
            sign_changes +=1
    return sign_changes

def fx_fnegx_coeff_list(coeff_list, fx=True):
    """calculate coefficients for f(x) and f(-x), note,
    the coeff list DOES include zero coefficients for
    all polynomial terms; the returned coeff_list will 
    need to be further processed to retain only non-zero 
    coefficients for polynomial terms of degree > 0"""
    degree  = get_degree(coeff_list)
    print('degree:',degree)
    if degree % 2 == 0:
        if fx:
            print("This is for f(x)")
            return coeff_list
        else:
            print("This is for f(-x)")
            for i in range(len(coeff_list)):
                if i % 2 != 0:
                    coeff_list[i] = -1*coeff_list[i]
            return coeff_list
    else:
        if fx:
            print("This is for f(x)")
            return coeff_list
        else:
            print("This is for f(-x)")
            for i in range(len(coeff_list)):
                if i % 2 == 0:
                    coeff_list[i] = -1*coeff_list[i]
            return coeff_list

def get_nonzero_coeff_list(x):
    last_element = x.pop()
    while 0 in x:
        x.remove(0)
    x.append(last_element)
    return x

def descarte_possibles(x):
    possible_zeros = list()
    if x == 0: return [0]
    for i in range(x):
        y = x-2*i
        if y >= 0: possible_zeros.append(y)
    return possible_zeros

def gen_descarte_summary(coeff_list_fx):
    """returns a dict of child dicts, where each
    child dict contains the keys 'rp', 'rn', 'c' and
    't', which represent the number of real positive, 
    real negative, complex, and total , respectively for a 
    coefficient list for all polynomial terms from degree 
    n, n-1,... , 0 (this implies, that polynomial terms
    with zero coeffients are included in the coefficient
    list supplied to this function!)
    """
    degree = get_degree(coeff_list_fx)
    coeff_list_fnegx = fx_fnegx_coeff_list(coeff_list_fx.copy(), False)
    nz_coeff_list_fx = get_nonzero_coeff_list(coeff_list_fx.copy())
    nz_coeff_list_fnegx = get_nonzero_coeff_list(coeff_list_fnegx.copy())
    real_pos_roots_max = get_descarte_signs(nz_coeff_list_fx)
    real_neg_roots_max = get_descarte_signs(nz_coeff_list_fnegx)
    real_pos = descarte_possibles(real_pos_roots_max)
    real_neg = descarte_possibles(real_neg_roots_max)
    combos=list(product(real_pos,real_neg))
    k = ['rp', 'rn', 'c', 't']
    combo_dict = dict.fromkeys(k)
    results = dict()
    for i in range(len(combos)):
        result_dict = combo_dict.copy()
        result_dict['rp'] = combos[i][0]
        result_dict['rn'] = combos[i][1]
        result_dict['c'] = degree - (combos[i][0] + combos[i][1])
        result_dict['t'] = degree
        results[i] = result_dict
    return results
        
def get_every_other_list_element(x:list, pos=True):
    every_other_element = list()
    for i in range(len(x)):
        if i % 2 == 0:
            every_other_element.append(x[i])

    if pos:

        greater_0 = list(filter(lambda x: x >=0, every_other_element))
        if len(greater_0) == len(every_other_element):
            return True
        return False

    else:
        greater_0 = list(filter(lambda x: x <=0, every_other_element))
        if len(greater_0) == len(every_other_element):
            return True
        return False


def check_poly_boundary(qr: list, upper=True) -> bool:
    """Suppose that f(x) is a polynomial with real coefficients
    and positive leading coefficient, and that f(x) is divided
    synthetically by x-c:
        i.) if c > 0 and if all numbers in the third row of the division
        process are either positive or zero, then c is an upper bound for
        the real solutions of the equation f(x) = 0
        
        ii.) If c < 0 and if the numbers in the third row of the
        division process are alternately positive and negative (
        where a 0 in the third row is considered to be either 
        positive or negative), the nc is a lwoer bound for the 
        real solutions of the equation f(x) = 0"""
    
    if upper:
        greater_0 = list(filter(lambda x: x >=0, qr))
        if len(greater_0) == len(qr):
            return True
        return False
    else:
        if qr[0] > 0:
            return get_every_other_list_element(qr[1:],pos=False) and \
                get_every_other_list_element(qr[0:])
        elif qr[0] < 0:
            return get_every_other_list_element(qr[1:]) and \
                get_every_other_list_element(qr[0:],pos=False)
        
def check_bounds_synthetic(c,dividend):
    """Given a first order polynombial divisor 'x-c', and dividend
    provided as a complete list of polynomial coefficients for a 
    polynomial of degree greater than 1, will print statements
    specifying whether or not 'c' is an upper or lower bound
    for the real roots of the given polynomial"""
    
    qr = synthetic_division(c,dividend)
    if c > 0:
        if check_poly_boundary(qr):
            print(f"{c} is an upper bound for real roots of the polynombial {poly_display_from_list(dividend)}")
        else:
            print(f"{c} is ***NOT*** an upper bound for real roots of the polynombial {poly_display_from_list(dividend)}")
    else:
        if check_poly_boundary(qr, False):
            print(f"{c} is a lower bound for real roots of the polynombial {poly_display_from_list(dividend)}")
        else:
            print(f"{c} is ***NOT*** an lower bound for real roots of the polynombial {poly_display_from_list(dividend)}")


def get_deg4_poly_from_mult2_roots(c1,c2):
    a4 = 1
    a3 = -2*(c1+c2)
    a2 = ((c1**2) + (4*(c1*c2)) + (c2**2))
    a1 = -2*(((c1**2)*c2) + (c1*(c2**2)))
    a0 = (c1**2)*(c2**2)
    return [a4, a3, a2, a1, a0]

def get_deg3_poly_from_roots(c1,c2,c3):
    a3 = 1
    a2 = -1*(c1+c2+c3)
    a1 = c1*c3 + c2*c3 + c1*c2 
    a0 = -1*(c1*c2*c3)
    return [a3, a2, a1, a0]
    
def do_sec3_5_ex1_6(c1,c2,c3,x,fx):
    coeff_list = get_deg3_poly_from_roots(c1,c2,c3)
    a = fx/eval_poly3(x,coeff_list)
    final_coeffs = mult_coeffs(coeff_list,a)
    poly = poly_display_from_list(final_coeffs)
    return coeff_list, a, final_coeffs, poly


def get_binomial(a,b,n):
    '''returns the sum from k = 0 to n for 
    (n choose k)*a**(n-k)*b**k'''
    from math import comb

    binom_coeffs = list()
    a_exponents = list()
    b_exponents = list()
    sum = 0
    for k in range(n+1):
        binom_coeffs.append(comb(n,k))
        a_exponents.append((n-k))
        b_exponents.append(k)
        sum += (comb(n,k))*(a**(n-k))*(b**k)
    return sum, binom_coeffs, a_exponents, b_exponents
    
def display_binomial(a,b,n):
    '''returns the string form of an expanded binomial
    of the form (a+b)**n'''
    _, binom_coeffs, a_exponents, b_exponents = get_binomial(a,b,n)
    poly = ''
    for i, (co,ax,bx) in enumerate(zip(binom_coeffs,a_exponents,b_exponents)):
        if i == 0:
            poly += '{}*(a**{})*(b**{})'.format(co,ax,bx)
        else:
            poly += ' + {}*(a**{})*(b**{})'.format(co,ax,bx)
    return poly    
    
class PolyFuncs:

    def __init__(self,degree=None) -> None:
        self.degree = degree
        self.poly_build_units = dict(add=list(), mult=list())
        
    def poly_add(self):
        pass

    def poly_mult(self):
        pass

class PolyTerm():

    """ {c-alpha-degree}
    
    j-x-n + k-x-n := (j+k)-x-n
    j-x-n + k-x-z := {'add': [(j-x-n, k-x-n)]}
    
    j-x-n + k-y-n := {'add': [(j-x-n, k-y-n)]}
    j-x-n + k-y-z := {'add': [(j-x-n, k-y-z)]}

    j-x-n * k-x-n := (j*k)-x-(n+n)
    j-x-n * k-x-z := (j*k)-x-(n+z)
    
    j-x-n * k-y-n := {'mult': [(j*k, x-n, y-n)]}
    j-x-n * k-y-z := {'mult': [(j*k, x-n, y-z)]}
    
    """


    def __init__(self,coefficient,alpha,degree):
        self.poly_funcs = PolyFuncs()
        self.coefficient = coefficient
        self.alpha = alpha
        self.degree = degree

    def __str__(self):
        return f'{self.coefficient}*{self.alpha}**{self.degree}'

    def add_poly_terms(self,term):
        if self.alpha == term.alpha and self.degree == term.degree:
            term_ = PolyTerm(self.coefficient+term.coefficient,self.alpha,self.degree) 
            return self.poly_funcs.poly_build_units['add'].append((term_,))
        else:
            return self.poly_funcs.poly_build_units['add'].append((self, term))
            

    def multiply_poly_terms(self,term):
        if self.alpha == term.alpha:
            term_ = PolyTerm(self.coefficient*term.coefficient,self.alpha,self.degree+term.degree) 
            return self.poly_funcs.poly_build_units['add'].append((term_,))
        else:
            return self.poly_funcs.poly_build_units['mult'].append((self.coefficient*term.coefficient, PolyTerm(1,self.alpha,self.degree), PolyTerm(1,term.alpha, term.degree)))
            

if __name__ == '__main__':

    real_pos = descarte_possibles(4)
    print(real_pos)

    # _,c,a,b = get_binomial(1,1,4)
    # divisor = [value*((1)**(idx)) for idx,value in enumerate(c[:])]
    # dividend = [1,1,-6,-14,-11,-3]
    # qx, rx = list_poly_div(divisor,dividend,q=[],n=0)
    # qx_poly = poly_display_from_list(qx)

    # def recursive_syn_div(c,dividend,depth=0,results=dict()):
    #     result = synthetic_division(c,dividend)
    #     results[depth] = result
    #     if result[-1] != 0:
    #         return results[depth-1][:-1], depth
    #     else:
    #         depth +=1
    #         return recursive_syn_div(c,result[:-1],depth,results)

    # qx_r = recursive_syn_div(-1,dividend)

    # print(f'''
    # qx: {qx}
    # qx_poly: {qx_poly}
    # qx_r: {qx_r}
    # rx: {rx}''')
        
    # c1 = eval(input("Input the first root: "))
    # c2 = eval(input("Input the 2nd root: "))
    # c3 = eval(input("Input the 3rd root: "))
    # x = eval(input("The value at which the polynomial is evaluated: "))
    # fx = eval(input("The value of the polynomial evaluated at 'x': "))
    # f = get_deg3_poly_from_roots
    # g = f(c1,c2,c3)
    # a = fx/eval_poly3(x,g)
    # final_coeffs = mult_coeffs(g,a)
    # poly = poly_display_from_list(final_coeffs)
    # print(f'''
    # g_coeffs: {g}
    # g(x): {poly_display_from_list(g)}
    # a: {a}
    # final_coeffs: {final_coeffs}
    # final_poly: {poly}
    # ''')

    # x = [x for x in range(1,6)]
    # x1 = [x*(-1)**n for n,x in enumerate(range(1,6))]
    # x2 = [x*(-1)**(n+1) for n,x in enumerate(range(1,6))]

    # xs = [x,x1,x2]
    # for e in xs:
    #     print(f'list: {e}')
    #     print(f'check upper: {check_poly_boundary(e)}')
    #     print(f'check lower: {check_poly_boundary(e,upper=False)}')


    # coeff_list_fx = [3,0,4,0,2,-5]
    # x = gen_descarte_summary(coeff_list_fx)
    # for v in x.values():
    #     print(v)
    # coeff_list_fnegx = fx_fnegx_coeff_list(coeff_list_fx.copy(), False)
    # nz_coeff_list_fx = get_nonzero_coeff_list(coeff_list_fx.copy())
    # nz_coeff_list_fnegx = get_nonzero_coeff_list(coeff_list_fnegx.copy())
    # real_pos_roots_max = get_descarte_signs(nz_coeff_list_fx)
    # real_neg_roots_max = get_descarte_signs(nz_coeff_list_fnegx)
    # fx = poly_display_from_list(coeff_list_fx)
    # fnegx = poly_display_from_list(coeff_list_fnegx)
    # print(f"""
    # for the polynomial f(x): 
        
    #     {fx}
    
    # By Descartes' Rule of Signs:
    # there are at most {real_pos_roots_max} pos
    # itive real roots.
    
    # by evaluating f(-x), we get the polynomial: 

    #     {fnegx}
    
    # from the polynomial form of f(-x), we see, again by Descartes' Rule 
    # of Signs, that there are at most {real_neg_roots_max} negative 
    # real roots.    
    # """)

    '''
I'm studying pre-calculus, and in my mathbook there is the following theorem which is the basis for my question:

If $f(x)$ is a polynomial of degree $n\space >\space 0$, then there exists n complex numbers, $c_1, c_2, ..., c_n$ such that:

$$ f(x) = a(x-c_1)(x-c_2)\cdots(x-c_n)$$

where $a$ is the leading coefficient of $f(x)$.  Each number $c_j$ is a zero of $f(x)$.

Here's the question:

   $c_1 = \sqrt{2},\space c_2=\pi,\space c3 = 0; f(0)=0$

I need to find a polynomial of degree 3 with the given zeros $c_1,\space c_2,\space c_3$

so when I plug in the zeros into the formula given in the theorem, I get:

$$f(x) = a(x-\sqrt{2})(x-\pi)(x-0)$$

$$f(x) = a(x-\sqrt{2})(x-\pi)(x)$$

$$f(x) = a[(x^3+(-\sqrt{2}-\pi)(x^2)+\sqrt{2}\pi x]$$

then evaluating our polynomial at $x=0:$

$$f(0) = a[0] = 0$$

Does this implies $a$ can be any real number?

If so, would that imply 

'''
