#Updating the list
list = [1, 2, 3, 4, 5]
list[1] = 33
list[4] = 22
print(list)
#Time Complexity:
#Space Complexity


#Time Complexity: O(n)
#Space Complexity: O(1)
list.insert(0, 12) #index, value -> inserts an element at any given index
print(list)

list.insert(4, 55)
print(list)

#Time Complexity: O(1)
#Space Complexity: O(1)
list.append(22)
print(list)

#Time Complexity: O(n), n is the length of the newlist
#Space Complexity: O(n)
newList = [1, 1, 1]
list.extend(newList)
print(list)