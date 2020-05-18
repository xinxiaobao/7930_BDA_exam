
dataSet = []
labels = []
with open('./decision_tree_data.dat', 'r') as f:
    data = f.readlines()
    labels = data[0].split()
    for line in data[1:]:
        dataSet.append(list(line.split()))
    # labels.append(f.readlines().split())
    # for line in f.readlines():
    #     dataSet.append(list(line.split()))

print(labels)
print(dataSet)