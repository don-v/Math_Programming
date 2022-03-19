from Ch3.x03_04_complex import *

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

if __name__ == '__main__':
    coeff_list_fx = [2,-7,0,3,6,-5]
    coeff_list_fnegx = fx_fnegx_coeff_list(coeff_list_fx.copy(), False)
    nz_coeff_list_fx = get_nonzero_coeff_list(coeff_list_fx.copy())
    nz_coeff_list_fnegx = get_nonzero_coeff_list(coeff_list_fnegx.copy())
    real_pos_roots_max = get_descarte_signs(nz_coeff_list_fx)
    real_neg_roots_min = get_descarte_signs(nz_coeff_list_fnegx)
    fx = poly_display_from_list(coeff_list_fx)
    fnegx = poly_display_from_list(coeff_list_fnegx)
    print(f"""
    for the polynomial f(x): 
        
        {fx}
    
    By Descartes' Rule of Signs:
    there are at most {real_pos_roots_max} positive real roots.
    
    by evaluating f(-x), we get the polynomial: 

        {fnegx}
    
    from the polynomial form of f(-x), we see, again by Descartes' Rule 
    of Signs, that there are at most {real_neg_roots_min} negative 
    real roots.    
    """)