from Ch3.x03_06_rc_zeros import *

'''
A function f is a **rational function** if, for all x in its
domain:

f(x) = g(x)/h(x)

where g(x) and h(x) aer polynomials. Of majoer importance are
the zeros of the numerator and denominator. _Throughout this
section we shall assume that g(x) and h(x) have no common factors,
and hence, no common zeros. 

Note that f(c) = 0 if and only if g(c) = 0, and hence the zeros
of the numerator g(x) are teh zeros of f(x).

However, if c is a zero of the demonimator, h(x), then
f(c) = g(c)/0 is undefined, and hence the behavior of f(x) 
requires special attention when x is near c!
'''

def fx_near_c(c, gx=[], hx=[], inc=0.1):
    lb = int(c-1)
    ub = int(c+1)
    r = range(lb, ub, inc)
    results = dict()
    for i in r:
        g = eval_poly3(i,gx)
        h = eval_poly3(i,hx)
        results[i] = g/h
    return results




if __name__ == '__main__':
    gx = [1]
    hx = [1,-2]
    close = fx_near_c(2,gx,hx)
    for k,v in close.items():
        print('{}: {}'.format(k,v))