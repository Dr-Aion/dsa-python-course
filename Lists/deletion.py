list = ['a', 'b', 'c', 'd', 'e']
# print(list[0:2])
# print(list[:2])
# print(list[2:])
# list[0:3] = ['x', 'y']
# print(list.pop(1)) #deletes certain element     Time Complexity: O(n)
# print(list.pop())  #deletes the last element    Time Complexity: O(1)
del list[0:2] # deletes the first 2 elements      Time Complexity: O(n)
list.remove('c')    #Time Complexity: O(1)
print(list[:])

#Space Complexity: O(1)