myDict = {'name': 'Edy', 'age': 26}
myDict['age'] = 27
print(myDict)
#Time Complexity: O(1)
#Space Complexity: O(1)

#if the key exists it updates the value, if not it creates the key-value pair
myDict['address'] = 'London'
print(myDict)
#Time Complexity: O(1)
#Space Complexity: amortized O(1)