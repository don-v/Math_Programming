from Ch3.x03_04_complex import *

def is_pos(x):
    """returns a boolean value for testing if x is positive"""
    return x > 0

def get_two(x,n):
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
    False"""
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

def get_nonzero_coeff_list(coeff_list, fx=True):
    """calculate coefficients for f(x) and f(-x)"""
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

def get_even_idx(list):
    pass


if __name__ == '__main__':
    x = [x for x in range(4)]
    doubles = get_two(x,2)
    print(doubles)
    