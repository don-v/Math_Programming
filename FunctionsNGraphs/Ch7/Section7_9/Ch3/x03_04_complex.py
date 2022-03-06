from Ch3.x03_03_synthetic_div import *
import cmath

if __name__ == '__main__':
    a=3
    b=4
    z1 = complex(a,b)
    z2 = z1.conjugate()
    sum_squares = a**2 + b**2
    conj_product = z1*z2
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'z1: {z1}')
    print(f'z2: {z2}')
    print(f'z1*z2 = {conj_product}')
    print(f'a**2 + b**2: {sum_squares}')
    print(f'does a**2 + b**2 == z1*z2: {sum_squares == conj_product}')
    
