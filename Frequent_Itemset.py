# Frequent Itemsets
from pymining import itemmining, assocrules

# set parameters
min_sup = 4
min_conf = 0.6

# input data
data = []
with open('./Frequent_Itemset.dat', 'r') as f:
    for line in f.readlines():
        data.append(list(line.split()))
        
transactions = data


relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=min_sup)

# print(report)
print('\n============== Frequent Itemsets ================\n')
for r, n in report.items():
    print(r, n)

# for key, value in report.items():
#     if value == 5:
#         print(key)

print('\n\n\n============== confidence ================\n')

rules1 = assocrules.mine_assoc_rules(report, min_support=min_sup, min_confidence=min_conf)
# print(rules1)
for i in rules1:
    print(i)