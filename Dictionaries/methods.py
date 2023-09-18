myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

#clear returns by default None
#myDict.clear() #deletes all the key-value pairs
#print(myDict)

newDict = myDict.copy() #retursns a shallow copy of the dictionary, a new dict is created 
print(myDict)
print(newDict)

#creates a new dictionary from given sequence of elements with value provided by user, the same values
#syntax: dictionary.fromkeys(sequence[], value)
newDict2 = {}.fromkeys([1, 2, 3], 0)
print(newDict2)

#get() return the value for the specified key if the key is in the dictionary
#dictionary.get(key, value)
print(myDict.get('city', 27))
print(myDict)

#items() returns a a view object that displays a list of dictionaries, key value tuple pairs
#dictionary.items()
print(myDict.items())

#keys() return a view object that displays the list of all keys in the dictionary
#dictionary.keys()
print(myDict.keys())

#the last element is removed, the key and the value are returned
print(myDict.popitem())

#setdefault() return the value of key if key is in the dictionary, if not it insets key with a value to the dictionary
#setdefault(key, default_value)
print(myDict.setdefault('name', 'Aigo'))
print(myDict)
print(myDict.setdefault('name1', 'Aigo'))
print(myDict)

#pop(key) deletes the pair by its key. None is the default value in case the key isn't found
removedElement = myDict.pop('age', None) 
print(removedElement)

#values() return a view object that display a list of values in the dictionary
print(myDict.values())

#update() updates the dictionary with the elements from another dictionary object or from an iterable of key value pairs
#update method adds elelments to the dictionaryif the key is not in the dictionary, else it updates the key value with the new value
newDict3 = {'a': 1, 'b': 2, 'c': 3}
myDict.update(newDict3)
print(myDict)