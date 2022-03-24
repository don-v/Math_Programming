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
        x = x-2*i
        if x >= 0: possible_zeros.append(x)
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
        
def check_poly_boundary(qr: list, bound='upper') -> bool:
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
    
    if bound:
        if all(qr) >=0:
            return True
    else:
        if qr[0] > 0:
            return get_every_other_list_element(qr[1:],pos=False)
        elif qr[0] < 0:
            return get_every_other_list_element(qr[1:])
        

def get_every_other_list_element(x:list, pos=True):
    every_other_element = list()
    for i in range(len(x)):
        if i % 2 == 0:
            every_other_element.append(x[i])

    if pos:
        return all(every_other_element) >= 0
    else:
        return all(every_other_element) <= 0



if __name__ == '__main__':
    coeff_list_fx = [3,0,4,0,2,-5]
    x = gen_descarte_summary(coeff_list_fx)
    for v in x.values():
        print(v)
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