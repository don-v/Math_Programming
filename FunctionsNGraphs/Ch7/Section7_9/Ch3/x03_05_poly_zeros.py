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
            print(f'{i}:{n_slice}')
            doubles.append((n_slice[0],n_slice[1]))
            i += 1
    return None

def get_descarte_signs(x: list) -> int:
    """takes non-zero coefficients of a polynomial 2
    at a time and determines if there is a sign change
    between the two coefficients"""
    pass


if __name__ == '__main__':
    x = [x for x in range(4)]
    get_two(x,2)
    