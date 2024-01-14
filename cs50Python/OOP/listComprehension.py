list1 = [1, 2, 3]
# list2 = [i * 3 for i in list1]
list2 = []
for i in range(len(list1)): 
    list2.append(list1[i] * 3)
print(list2)