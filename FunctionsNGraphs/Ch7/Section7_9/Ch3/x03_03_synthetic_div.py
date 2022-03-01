from Ch3.x03_02_polynomial_div import *

def list_poly_div(c1,c2,q=[],n=0):
    """
    a recursive function that carries out polynomial division,
    where c1 represents the divisor, and c2 the dividend, and
    returns the quotient and remainder of the division

    both c1, and c2 are lists of polynomial coefficients, ordered
    in decreasing degree with increasing list index
    """
    d1,d2 = get_degree(c1), get_degree(c2)
    co1,co2 = c1,c2
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
        c2_ = rx
        return list_poly_div(c1,c2_,q,n)

def synthetic_division(c,dividend):
    '''c is the real number in the factor "x-c"; 
    dividend is the list of polynomial coefficient for
    the dividend, including "0"s for "missing' coefficient
    terms. the coefficients correspond to polynomial terms in 
    decreasing degree order with increasin list index. '''
    row1=dividend.copy()
    row2=[0]
    row3=row2.copy()
    for i in range(len(dividend)):
        if i == 0:
            row3[i] = row1[i]
        else:
            row2.append(c*row3[i-1])
            row3.append(row1[i] + row2[i])
    return row3



if __name__ == '__main__':
    c1 = 2
    c2 = [3,-8,0,9,5]
    row3 = synthetic_division(c1,c2)
    print(row3)
    