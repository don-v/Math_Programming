from elim_04102021 import *

np.set_printoptions(precision=3, suppress=True)

mat19 = np.array(
    [
    [2, -1, -2, 2, -5, 2],
    [1, 3, -2, 1, -2, -5],
    [-1, 4, 2, -3, 8, -4],
    [3, -2, -4, 1, -3, -3],
    [4, -6, 1, -2, 1, 10]
    ]
    ).astype(float)

# ech19 = to_echelon(mat19)
# Abx19 = echelon_solver(ech19)
# print('A:\n', Abx19[0])
# print(f'Ax:\n {Abx19[0] @ Abx19[1]} \nb:\n {Abx19[2]}')

# q_plus_kp(-0.5, 1, 2, mat19)
# q_plus_kp(0.5, 1, 3, mat19)
# kq(2,2,mat19)
# kq(2,3,mat19)
# q_plus_kp(-1.5, 1, 4, mat19)
# q_plus_kp(-2, 1, 5, mat19)
# kq(2,4,mat19)
# q_plus_kp(-1, 2, 3, mat19)
# q_plus_kp((1/7), 2, 4, mat19)
# kq(7,4,mat19)
# q_plus_kp((4/7), 2, 5, mat19)
# kq(7,5,mat19)
# q_plus_kp(4, 3, 4, mat19)
# q_plus_kp((-27/4), 3, 5, mat19)
# kq(2,5,mat19)
# q_plus_kp((-30/44), 4, 5, mat19)
# kq(44,5,mat19)

# echelon_solver(mat19)

mat20 = np.array(
    [
    [3, 2, 1, 3, 1, 1, 1],
    [2, 1, -2, 3, -1, 4, 6],
    [6, 3, 4, -1, 2, 1, -6],
    [1, 1, 1, 1, -1, -1, 8],
    [-2, -2, 1, -3, 2, -3, -10],
    [1,-3, 2, 1, 3, 1, -1]
    ]
    ).astype(float)


# q_plus_kp((-2/3),1,2,mat20)
# kq(3,2,mat20)
# q_plus_kp(-2,1,3,mat20)
# q_plus_kp((-1/3),1,4, mat20)
# kq(3,4, mat20)
# q_plus_kp((2/3),1,5,mat20)
# kq(3,5,mat20)
# q_plus_kp((-1/3),1,6,mat20)
# kq(3,6,mat20)
# q_plus_kp((-1),2,3,mat20)
# q_plus_kp((1),2,4,mat20)
# q_plus_kp((-2),2,5,mat20)
# q_plus_kp((-11),2,6,mat20)
# q_plus_kp((6/10),3,4,mat20)
# kq(10,4,mat20)
# q_plus_kp((-21/10),3,5,mat20)
# kq(10,5,mat20)
# q_plus_kp((-93/10),3,6,mat20)
# kq(10,6,mat20)
# q_plus_kp((120/30),4,5,mat20)
# kq(30,5,mat20)
# q_plus_kp((600/30),4,6,mat20)
# kq(30,6,mat20)
# q_plus_kp((-31050/4950),5,6,mat20)
# kq(4950,6,mat20)

# echelon_solver(mat20)


# ech20 = to_echelon(mat20)
# Abx20 = echelon_solver(ech20)
# print('A:\n', Abx20[0])
# print(f'Ax:\n {Abx20[0] @ Abx20[1]} \nb:\n {Abx20[2]}')

# q_plus_kp((-2/3),1,2,mat20)
# kq(3,2,mat20)



mat21 = np.array(
    [
    [5, 0, 2, 1],
    [0, 1, -3, 2],
    [2, 1, 0, 3]    
    ]
    ).astype(float)


# ech21 = to_echelon(mat21)
# echelon_solver(ech21)


mat22 = np.array(
    [
    [2, -5, 0, 4],
    [0, 3, 2, -3],
    [7, 0, -3, 1]    
    ]
    ).astype(float)

# ech22 = to_echelon(mat22)
# echelon_solver(ech22)

mat23 = np.array(
    [
    [4, -3, 1],
    [2, 1, -7],
    [-1, 1, -1]    
    ]
    ).astype(float)

# ech23 = to_echelon(mat23)
# echelon_solver(ech23[0:2,:])

mat24 = np.array(
    [
    [2, 3, -2],
    [1, 1, 1],
    [1, -2, 13]    
    ]
    ).astype(float)

# ech24 = to_echelon(mat24)
# echelon_solver(ech24[0:2,:])

mat27 = np.array(
    [
    [.05, .1, .25, 8],
    [1, 1, 1, 72],
    [1, 0, -2, 0]    
    ]
    ).astype(float)

# ech27 = to_echelon(mat27)
# echelon_solver(ech27)


mat28 = np.array(
    [
    [69, -21, -30, 0],
    [-99, 0, 99, 99],
    [-1, 1, -1, -3]    
    ]
    ).astype(float)

# ech28 = to_echelon(mat28)
# echelon_solver(ech28)

mat29 = np.array(
    [
    [.1, .3, .5, 16],
    [1, 1, 1, 50],
    [0, -2, 1, 0]    
    ]
    ).astype(float)

# ech29 = to_echelon(mat29)
# echelon_solver(ech29)

mat30 = np.array(
    [
    [8, 0, 0, 1],
    [6, 0, 6, 1],
    [0, 10, 10, 1]    
    ]
    ).astype(float)


# q_plus_kp((-6/8),1,2,mat30)
# kq(8,2,mat30)
# pqexchange(2,3,mat30)

# sol30 = echelon_solver(mat30)
# print('hours:', f'{1/(sum(sol30[1]))}')

mat31 = np.array(
    [
    [6, 6, 0, 4500],
    [8, 0, 8, 3600],
    [0, 7, 7, 4900]    
    ]
    ).astype(float)


# q_plus_kp((-8/6),1,2,mat31)
# kq(6,2,mat31)
# q_plus_kp((7/48),2,3,mat31)
# kq(48,3,mat31)

# sol31 = echelon_solver(mat31)
# print('hours:', f'{1000/sol31[1]}')

mat32 = np.array(
    [
    [1, 1, 0, (1/48)],
    [0, 1, 1, (1/80)],
    [1, 0, 1, (1/60)]    
    ]
    ).astype(float)


# pqexchange(2,3,mat32)
# q_plus_kp(-1,1,2,mat32)
# q_plus_kp(1,2,3,mat32)

# sol32 = echelon_solver(mat32)
# print('resistances:', f'{1/sol32[1]}')


mat33 = np.array(
    [
    [.3, .2, .15, (.25*600)],
    [1, 1, 1, 600],
    [0, -1, 1, 100]    
    ]
    ).astype(float)

# q_plus_kp((-10/3),1,2,mat33)
# kq(3,2,mat33)
# q_plus_kp(1,2,3,mat33)

# echelon_solver(mat33)

mat34 = np.array(
    [
    [(1/8), .5, 1, 7],
    [.5, 1, 1, 11],
    [(9/8), (3/2), 1, 17]    
    ]
    ).astype(float)

# q_plus_kp(-4,1,2,mat34)
# q_plus_kp(-9,1,3,mat34)
# q_plus_kp(-3,2,3,mat34)

# echelon_solver(mat34)

mat35 = np.array(
    [
    [4, 2, 1, (5/2)],
    [1, 1, 1, 3],
    [1, -1, 1, 1]    
    ]
    ).astype(float)

# q_plus_kp((-1/4),1,2,mat35)
# q_plus_kp((-1/4),1,3,mat35)
# q_plus_kp(3,2,3,mat35)

# echelon_solver(mat35)

mat36 = np.array(
    [
    [-1, -1, 1, 22],
    [8, 2, 1, 13],
    [-27, -3, 1, -12]    
    ]
    ).astype(float)

# q_plus_kp(8,1,2,mat36)
# q_plus_kp(-27,1,3,mat36)
# q_plus_kp(4,2,3,mat36)

# echelon_solver(mat36)

mat37 = np.array(
    [
    [2, 1, 1, -5],
    [-1, -4, 1, -17],
    [3, 0, 1, -9]    
    ]
    ).astype(float)

# ech37 = to_echelon(mat37)
# echelon_solver(ech37)

mat38 = np.array(
    [
    [9, 3, 1, -1],
    [1, 1, 1, -7],
    [4, -2, 1, 14]    
    ]
    ).astype(float)

ech38 = to_echelon(mat38)
echelon_solver(ech38)