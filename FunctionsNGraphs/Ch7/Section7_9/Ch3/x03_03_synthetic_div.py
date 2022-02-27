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

if __name__ == '__main__':
    c1 = [1,-2]
    c2 = [3,-8,0,9,5]
    qx,rx = list_poly_div(c1,c2)
    print('qx:', qx)
    print('rx:', rx)
    