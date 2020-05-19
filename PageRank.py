# Q1 b
import numpy as np 

# input data
A = []
with open('./PageRank_data.dat', 'r') as f:
    for line in f.readlines():
        A.append(list(map(int, line.split())))


A = np.array(A)
ATD = A.T/A.T.sum(axis = 0)
n = len(A[0])
ce = [1/n] * n
ce = np.array(ce).T

print('\n ======== initial directed graph ======== \n')     
print(A)
print('\n\n\n ======== ATD ======== \n')   
print(ATD)

print('\n================== iteration results =====================\n')
print('initial ce:', ce)
m = 20
for i in range(m):
    ce = ATD @ ce
    # print('Iteration'+ str(i+1), ':',ce)
print('==============================================')
# print(ce)


# beta without S
# input beta
beta = 0.8
ce = [1/n] * n


M = (1 - beta)/n + beta*ATD
print('\n\n\n ======== M no S ======== \n')  
print(M)
for i in range(m):
    ce =M @ ce
    # print('Iteration'+ str(i+1), ':',ce)

# beta with S
# input S and beta
ce = [1/n] * n
beta = 0.8
s = [1, 0, 0, 0]

s_num = len(s)
s_n = 1
s = np.array(s).reshape(s_num, 1)

AM = (s*(1 - beta)/s_n) + beta*ATD
for i in range(m):
    ce =AM @ ce
    # print('Iteration'+ str(i+1), ':',ce)
print('\n\n\n ======== M with S ======== \n')  
print(AM)

print('result:', ce)