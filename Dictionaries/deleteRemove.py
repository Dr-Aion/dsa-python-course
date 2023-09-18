myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

#Time Complexity: O(1) it involves the Hash Table
#Space Complexity: O(1)
#del myDict['age'] 
#print(myDict)


#Time Complexity: O(1) it involves the Hash Table
#Space Complexity: O(1)
# removedElement = myDict.pop('age', None) #None is the default value in case the key isn't found
# print(removedElement)

#Time Complexity: O(1) it involves the Hash Table
#Space Complexity: O(1)
removedElement = myDict.popitem() #the last element is removed, the key and the value are returned
print(removedElement)

#Time Complexity: O(n)
#Space Complexity: O(1)
myDict.clear() #deletes all key-value pairs of the dictionary