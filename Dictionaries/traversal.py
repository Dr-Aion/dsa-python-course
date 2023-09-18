myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(myDict)
#Time Complexity: O(n)
#Sapce Complexity: O(1)