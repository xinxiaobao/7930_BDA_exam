# Q1 b
import numpy as np 

ATD = [[0, 0.5, 0.5],
        [0, 0, 0.5],
        [0, 0.5, 0]]


# ATD = [[0, 0.5, 0.5],
#         [0.5, 0, 0.5],
#         [0.5, 0.5, 0]]


ATD = [[0, 1/3, 0, 0.25, 0],
        [0, 0 , 1, 0.25, 0],
        [0.5, 0, 0, 0.25, 1],
        [0, 1/3, 0, 0, 0],
        [0.5, 1/3, 0, 0.25, 0]]

# ce = [2, 1/3, 1/3]
ce = [0.2, 0.2, 0.2, 0.2, 0.2,]

ATD = np.array(ATD)
ce = np.array(ce).T
# print(ATD, ce)
print('=======================================')


n = 20
for i in range(n):
    ce = ATD @ ce
    print('Iteration'+ str(i+1), ':',ce)
print('=========================')
# print(ce)


# Q1 c 
# m = 20
# for i in range(m):
#     ce = 0.04 + 0.8 * (ATD @ ce)
#     print('Iteration'+ str(i+1), ':',ce)


# print(np.array([1/3]*3))
# print([1/3]*3)