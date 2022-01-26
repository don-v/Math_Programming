"""
A function f is a polynomial if:

f(x) = a_{n}*x**n + a_{n-1}*x**(n-1) + ... + a_{1}*x + a_{0}

where the coefficients a_{0}, a_{1}, ... , a_{n} are real numbers and
the exponents are nonnegative integers

"""
import sys, time


def gen_coeffs(n=2):
    coeffs = dict()
    for x in range(n+1):
        coeffs[f'a{n}'] = int(input(f'the value of a{n} is: '))
    return coeffs

def gen_poly(n=2):
    if n==0: return f"c[f'a{n}']*x**{n}"
    else: return f"c[f'a{n}']*x**{n}" + ' + ' + gen_poly(n-1)
   
def eval_poly(p:str, c:dict, rangex:tuple):
    points = dict()
    for x in range(*rangex):
        points[x] = eval(p)
    return points
    

if __name__ == '__main__':
    start = time.perf_counter()
    if len(sys.argv) == 1:
        c = gen_coeffs()
        p = gen_poly()
        points = eval_poly(p,c,(-5,6))
        elapsed_time = time.perf_counter() - start
        print(f"""
        n={2}
        polynomial={p}
        elapsed time = {elapsed_time}
        points = {points}
        """)
    else:
        n = int(sys.argv[1])
        c = gen_coeffs(n)
        p = gen_poly(n)
        points = eval_poly(p,c,(-5,6))
        elapsed_time = time.perf_counter() - start
        print(f"""
        n={n}
        polynomial={p}
        elapsed time = {elapsed_time}
        points = {points}
        """)

