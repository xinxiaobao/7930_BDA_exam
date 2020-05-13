# Frequent Itemsets
from pymining import itemmining, assocrules

# input data
# transactions =  [
#         ['Mi','Be', 'Di'],
#         ['Br', 'Bu', 'Mi'],
#         ['Mi', 'Di', 'Co'],
#         ['Br', 'Bu', 'Co'],
        
#         ['Be', 'Co', 'Di'],
#         ['Mi', 'Di', 'Br', 'Bu'],
#         ['Br', 'Bu', 'Di'],
#         ['Be', 'Di'],
        
#         ['Mi', 'Di', 'Br', 'Bu'],
#         ['Be', 'Co']        
#     ]
# transactions =  [
#         ['m','c', 'b'],
#         ['m', 'p', 'j'],
#         ['m', 'c', 'b',  'n'],
#         ['c', 'j'],
        
#         ['m', 'p', 'b'],
#         ['m', 'c', 'b', 'j'],
#         ['c', 'b', 'j'],
#         ['b', 'c'],  
#     ]

data = []
with open('./Frequent_Itemset.dat', 'r') as f:
    for line in f.readlines():
        data.append(list(line.split()))
        
transactions = data

relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=2)

# print(report)
print('\n============== Frequent Itemsets ================\n')
for r, n in report.items():
    print(r, n)

# for key, value in report.items():
#     if value == 5:
#         print(key)

print('\n\n\n============== confidence ================\n')

rules1 = assocrules.mine_assoc_rules(report, min_support=3, min_confidence=0.6)
# print(rules1)
for i in rules1:
    print(i)