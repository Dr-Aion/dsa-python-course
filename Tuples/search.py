newTuple = ('a', 'b', 'c', 'd', 'e')

print('a' in newTuple) #Time Complexity: O(n)

print(newTuple.index('c')) #Time Complexity: O(n)

def searchTuple(pTuple, element):
    for i in range(len(pTuple)):
        if pTuple[i] == element:
            return f"The element is found at {i} index"
    return 'The element is not found'
print(searchTuple(newTuple, 'b'))
#Time Complexity: O(n)
#Space Complexity: O(1)