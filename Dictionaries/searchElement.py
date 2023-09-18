myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'the value does not exits'
print(searchDict(myDict, 26))

#Time Complexity: O(n)
#Space Complexity: O(1)
