import numpy as np
from sklearn import preprocessing 

# input data
data = [100, 400, 600,800, 3000, 4200]
arr = np.array(data)


print('\n ========= min-max ===========\n')
# set min, max
min, max = 0, 1
for x in arr:
  x = float(x - np.min(arr))/(np.max(arr)- np.min(arr))
  print(x *(max - min)+ min)

print('\n\n\n ========= Z-score ===========\n')
print('mean:', arr.mean(),'      std:', arr.std())
for x in arr:
  x = float(x - arr.mean())/arr.std()
  print(x)

print('\n\n\n ========= statistics ===========\n')
print('median:',np.median(arr))
print('variance:', np.var(arr))
