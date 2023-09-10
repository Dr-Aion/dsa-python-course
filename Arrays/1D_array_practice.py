from array import *

#1. Create an array and traverse it
print("Task 1 Create an array and traverse it")
arr = array('i', [7, 2, 5, 1, 8])

for i in arr:
    print(i)

#2. Access individual elements through indexes
print("Task 2 Access individual elements through indexes")
print(arr[3])

#3. Append any value to the array using append() method
print("Task 3 Append any value to the array using append() method")
arr.append(9)
print(arr)

#4. Insert value in an array using insert() method
print("Task 4 Insert value in an array using insert() method")
arr.insert(4, 12)
print(arr)

#5. Extend python array using extend() method
print("Task 5 Extend python array using extend() method")
newArray = array('i', [10, 11, 12])
arr.extend(newArray)
print(arr)

#6. Add items from list into array using fromList() method
print("Task 6 Add items from list into array using fromList() method")
tempList = [20, 21, 22]
arr.fromlist(tempList)
print(arr)

#7. Remove any array element using remove() method
print("Task 7 Remove any array element using remove() method")
arr.remove(12)
print(arr)

#8. Remove last array element using pop() method
print("Task 8 Remove last array element using pop() method")
arr.pop()
print(arr)

#9. Fetch any element through its index using index() method
print("Task 9 Fetch any element through its index using index() method")
print(arr.index(11))

#10. Reverse a python array using a reverse() method
print("Task 10 Reverse a python array using a reverse() method")
arr.reverse()
print(arr)

#11. Get array buffer information