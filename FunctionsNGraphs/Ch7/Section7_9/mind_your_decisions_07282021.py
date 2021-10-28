# 90 % Fail Simple Logic Test:

# A sack contains 4 different colored balls:
# 14 balls are not blue
# 16 balls are not yellow
# 24 balls are not red
# 12 balls are not pink




# if 14 balls are not blue, then the maximum of 
# yellow, red or pink must be 14

# so yellow <=14, red <=14, pink <=14

combos_yrp = []
for yellow in range(1,13):
    for red in range (1,13):
        for pink in range (1,15):
            if yellow + red + pink == 14:
                combos_yrp.append({'yellow': yellow, 'red': red, 'pink': pink})
print('len yrp:', len(combos_yrp))


# if 16 balls not yellow, then maximum of
# blue, red, pink must be 16

# so blue <=16, red <=16, pink <=16

combos_brp = []
for blue in range(1,13):
    for red in range(1,13):
        for pink in range(1,15):
            if blue + red + pink == 16:
                combos_brp.append({'blue': blue, 'red': red, 'pink': pink})
print('len brp:', len(combos_brp))


# 24 balls are not red, implying that maximum
# number of balls for blue, yellow, pink cannot exceed
# 24

# so blue <=24, yellow <=24, and pink <=24

combos_byp = []
for blue in range(1,13):
    for yellow in range(1,13):
        for pink in range(1,15):
            if blue + yellow + pink == 24:
                combos_byp.append({'blue': blue,  'yellow': yellow, 'pink': pink})
print('len byp:', len(combos_byp))


# if 12 balls are not pink, then maximum of
# blue, yellow, and red cannot exceed 12

# blue <=12, yellow <=12, red <=12

combos_byr = []
for blue in range(1,13):
    for yellow in range(1,13):
        for red in range(1,13):
            if blue + yellow + red == 12:
                combos_byr.append({'blue': blue,  'yellow': yellow, 'red': red})
print('len byr:', len(combos_byr))


# so 
# blue <=12
# yellow <=12
# red <=12
# pink <=14



# blue, yellow, red, pink = 0,0,0,0






# common_by = []
# for byr in combos_byr:
#     for byp in combos_byp:
#         if (byp['blue'] == byr['blue']) and (byp['yellow'] == byr['yellow']) :
#                 common_by.append((byr, byp))
# print('len common_by:', len(common_by), '\n')
# print('common_by: \n', common_by)

# common_yr = []
# for yrp in combos_yrp:
#     for byr in combos_byr:
#         if (byr['red'] == yrp['red']) and (byr['yellow'] == yrp['yellow']) :
#                 common_yr.append((yrp, byr))
# print('len common_yr:', len(common_yr), '\n')
# print('common_yr: \n', common_yr)












# """
# 90 % Fail Simple Logic Test:

# A sack contains 4 different colored balls:
# 14 balls are not blue
# 16 balls are not yellow
# 24 balls are not red
# 12 balls are not pink


# if 14 balls are not blue, then the maximum of 
# yellow, red or pink must be 14

# so yellow <=14, red <=14, pink <=14

# if 16 balls not yellow, then maximum of
# blue, red, pink must be 16

# so blue <=16, red <=16, pink <=16

# 24 balls are not red, implying that maximum
# number of balls for blue, yellow, pink cannot exceed
# 24

# so blue <=24, yellow <=24, and pink <=24

# if 12 balls are not pink, then maximum of
# blue, yellow, and red cannot exceed 12

# blue <=12, yellow <=12, red <=12

# so 
# blue <=12
# yellow <=12
# red <=12
# pink <=14

# """
# from typing import final


# combos_yrp = []
# for yellow in range(1,13):
#     for red in range (1,13):
#         for pink in range (1,15):
#             if yellow + red + pink == 14:
#                 combos_yrp.append({'yellow': yellow, 'red': red, 'pink': pink})
# print('len yrp:', len(combos_yrp))

# combos_brp = []
# for blue in range(1,13):
#     for red in range(1,13):
#         for pink in range(1,15):
#             if blue + red + pink == 16:
#                 combos_brp.append({'blue': blue, 'red': red, 'pink': pink})
# print('len brp:', len(combos_brp))


# combos_byp = []
# for blue in range(1,13):
#     for yellow in range(1,13):
#         for pink in range(1,15):
#             if blue + yellow + pink == 24:
#                 combos_byp.append({'blue': blue,  'yellow': yellow, 'pink': pink})
# print('len byp:', len(combos_byp))

# combos_byr = []
# for blue in range(1,13):
#     for yellow in range(1,13):
#         for red in range(1,13):
#             if blue + yellow + red == 12:
#                 combos_byr.append({'blue': blue,  'yellow': yellow, 'red': red})
# print('len byr:', len(combos_byr))

# common_by = []
# for byr in combos_byr:
#     for byp in combos_byp:
#         if (byp['blue'] == byr['blue']) and (byp['yellow'] == byr['yellow']) :
#                 common_by.append((byr, byp))
# print('len common_by:', len(common_by), '\n')
# print('common_by: \n', common_by)

# common_yr = []
# for yrp in combos_yrp:
#     for byr in combos_byr:
#         if (byr['red'] == yrp['red']) and (byr['yellow'] == yrp['yellow']) :
#                 common_yr.append((yrp, byr))
# print('len common_yr:', len(common_yr), '\n')
# print('common_yr: \n', common_yr)

# # common_all = []
# # for byr,byp in common_by:
# #     for ypr,byr2 in common_yr:
# #         if (byp['yellow'] == ypr['yellow']) and (byp['pink'] == ypr['pink'])\
# #         and (byr['yellow'] == ypr['yellow']) and (byr['red'] == ypr['red']):
# #             common_all.append((byp,ypr))
# # print('len common_all:', len(common_all), '\n')
# # print('common_all: \n', common_all)

# # common_all = []
# # for byr,byp in common_by:
# #     for ypr,byr2 in common_yr:
# #         if (byp['yellow'] == ypr['yellow']) and (byp['pink'] == ypr['pink']):
# #         # and (byr['yellow'] == ypr['yellow']) and (byr['red'] == ypr['red']):
# #             common_all.append((byp,ypr))
# # print('len common_all:', len(common_all), '\n')
# # print('common_all: \n', common_all)
            
# # x = common_by[0]
# # print('\n', x)
# # print('type(x):', type(x))

# # combined = {}
# # for d in x:
# #     for key in d.keys():
# #         if key not in combined.keys():
# #             combined[key] = d[key]
# # print('\n', combined)

# def combined_common_y(y):
#     full_list = []
#     for tup in y:
#         combined = {}
#         for d in tup:
#             for key in d.keys():
#                 if key not in combined.keys():
#                     combined[key] = d[key]
#         full_list.append(combined)
#     print('\nfull_list: \n', full_list)
#     return full_list

# # combined_common_y(common_by)
# def final_list(y):
#     possible_combos = []
#     for d in y:
#     # 14 balls are not blue
#     # 16 balls are not yellow
#     # 24 balls are not red
#     # 12 balls are not pink
        

#     # if 14 balls are not blue, then the maximum of 
#     # yellow, red or pink must be 14

#     # so yellow <=14, red <=14, pink <=14
#         if d['yellow'] + d['red'] + d['pink'] ==14:
#     # if 16 balls not yellow, then maximum of
#     # blue, red, pink must be 16

#     # so blue <=16, red <=16, pink <=16
#             if d['blue'] + d['red'] + d['pink'] ==16:
#     # 24 balls are not red, implying that maximum
#     # number of balls for blue, yellow, pink cannot exceed
#     # 24

#     # so blue <=24, yellow <=24, and pink <=24
#                 if d['yellow'] + d['blue'] + d['pink'] ==24:
#     # if 12 balls are not pink, then maximum of
#     # blue, yellow, and red cannot exceed 12

#     # blue <=12, yellow <=12, red <=12
#                     if d['yellow'] + d['red'] + d['blue'] ==12:
#                         # print(d)
#                         possible_combos.append(d)
#     print('\nlength combo list: \n', len(possible_combos))
#     print('\npossible combos: \n',possible_combos)

# # so 
# # blue <=12
# # yellow <=12
# # red <=12
# # pink <=14
    
# final_list(combined_common_y(common_yr))
# final_list(combined_common_y(common_by))



