import numpy as np
from chapter7_funcs_src import *
from itertools import combinations

def q1(combo):
    x=combo[0]
    y=combo[1]
    p = 15*x + 8*y
    print(f"""
    the profit for {x} units of 'Set Point'
    and {y} units of 'Double Fault' is ${p}    
    """)

def q2(combo):
    x=combo[0]
    y=combo[1]
    p = 25*x + 30*y
    print(f"""
    the profit for {x} units of 'Deluxe' 
    and {y} units of 'Standard' is ${p}    
    """)


def q3(combo):
    x=combo[0]
    y=combo[1]
    p = 3*x + 4*y
    print(f"""
    the cost for {x} lbs. of 'S' 
    and {y} lbs. of 'T' is ${p:2}    
    """)


def q4(combo):
    x=combo[0]
    y=combo[1]
    p = .25*x + .15*y
    print(f"""
    the sales-cost difference for {x} units of NB 'M'
    and {y} units of NB 'N' is ${p:.2f}!    
    """)

def q5(combo):
    x=combo[0]
    y=combo[1]
    p = 1070+ 2*x + 4*y
    print(f"""
    the shipping cost for {x} units from warehouse W1 to A
    and {y} units from warehouse W1 to B is ${p:.2f}!    
    """)


def q6(combo):
    x=combo[0]
    y=combo[1]
    p = 125*x + 200*y
    print(f"""
    the total cost for {x} tons of coffee from supplier A
    and {y} tons of coffee from supplier B is ${p:.2f}!

    this would result in {0.2*x + 0.4*y} tons of premium coffee
    and {0.5*x + 0.2*y} tons of Regular coffee!    
    """)


def q7(combo):
    x=combo[0]
    y=combo[1]
    p = 86*x + 134*y
    print(f"""
    the total profit for {x} acres of crop A
    and {y} acres of crop B is ${p:.2f}!

    this would result in:
    {x + y} total acres of crop
    ${4*x + 6*y} in seed costs
    ${20*x + 10*y} in labor costs
    and ${110*x + 150*y} in income!    
    """)

def q8(combo):
    x=combo[0]
    y=combo[1]
    p = 20*x + 50*y
    print(f"""
    the total profit for {x} units of product A
    and {y} units of product B is ${p:.2f}!

    """)

def q10(combo):
    x=combo[0]
    y=combo[1]
    p = .25*x + .40*y
    print(f"""
    the total profit for {x} bags of peanuts
    and {y} bags of candy is ${p:.2f}!

    """)



combos = [(0,0), (0,400), (200,400), (400,300), (500,200), (500,0)]

# print([q1(x) for x in combos])

[q10(x) for x in combos]



# first figure out the sets that sum to 20
# then among those, figure out the ones that give percentages >= desired!s
# 

def sum20(n):
    sum20s=[]
    for x in range(0,n+1):
        for y in range(0,n+1):
            for z in range(0,n+1):
                if x+y+z == n:
                    sum20s.append((x,y,z))
    # print(sum20s)
    return sum20s

x=sum20(20)[0]
# print(x)

z = np.arange(4)
# print(z)
# print(z.shape)

Awt=np.array([0.2,0.2,0.1])
Bwt=np.array([0.1,0.4,0.2])
Cwt=np.array([0.25,0.15,0.25])


y = np.array([x])
# print(y)
# print(y.shape)
# print('dot',np.dot(y,Awt))

y = np.array([*x])
# print(y)
# print('*',np.dot(y,Awt))

# print('*dot',y.dot(Awt))

def A_pct(x):
    Awt=np.array([0.2,0.2,0.1])
    return np.dot(x,Awt)/sum(x) >= 0.14

def B_pct(x):
    Bwt=np.array([0.1,0.4,0.2])
    return np.dot(x,Bwt)/sum(x) >= 0.16

def C_pct(x):
    Cwt=np.array([0.25,0.15,0.25])
    return np.dot(x,Cwt)/sum(x) >= 0.20

def poss_sols(n):
    sols=[]
    for combo in sum20(n):
        if A_pct(combo) and B_pct(combo) and C_pct(combo):
            sols.append(combo)
    # print(sols)
    # print('\nlen:',len(sols))
    return sols

# len(poss_sols(20))

def profit():
    costs=np.array([0.25,0.35,0.5])
    profits={}
    for sol in poss_sols(20):
        profits[sol]=np.dot(sol,costs)
    min_max = {}
    for k,v in profits.items():
        if profits[k] == min(profits.values()):
            cost = f'${v:.2f}'
            min_max['min'] = k,cost
        if profits[k] == max(profits.values()):
            cost = f'${v:.2f}'
            min_max['max'] = k,cost
    print(min_max)
    return min_max


# profit()

def q9(combo):
    x=combo[0]
    y=combo[1]
    p = .25*x + .35*y
    print(f"""
    the total profit for {x} ounces of substance x
    and {y} ounces of product y is ${p:.2f}!

    """)


combos = [(10,10), (13.17,4.7), (16,4)]

# [q9(x) for x in combos]

zymat = mat_maker2((4,3), 0.2,0.1,2.8, 0.4,0.2,3.2, 0.15,0.25,4, 1,1,20)

# print(zymat)

mat_combos = combinations(range(4), 2)

# print(list(mat_combos))

# print([x for x in list(mat_combos) if x[1] == 3])

def sel_rows(tup, mat):
    return mat[tup, :]

def solve_all(mat):
    sols = {}
    mat_combos = combinations(range(4), 2)
    combos = [x for x in list(mat_combos) if x[1] == 3]
    for combo in combos:
        sols[combo] = echelon_solver(to_echelon(sel_rows(combo, mat)))[1]
    print(sols)
    return sols

def solve_all2(mat,n):
    sols = {}
    mat_combos = combinations(range(n), 2)
    # combos = [x for x in list(mat_combos) if x[1] == 3]
    for combo in mat_combos:
        sols[combo] = echelon_solver(to_echelon(sel_rows(combo, mat)))[1]
    print(sols)
    return sols


# solve_all(zymat)

mat = mat_maker2((3,3), 0.2,0.1,2.8, 0.4,0.2,3.2, 0.15,0.25,4) 

combos = [x for x in list(combinations(range(3),2))]

# for combo in combos:
#     echelon_solver(to_echelon(mat[combo,:]))[1]