#in/not operators
myDict = {
    3: "three",
    4: "four",
    5: "five",
    9: "nine",
    2: "two",
    1: "one"
}

print(3 in myDict) #in operator works with keys
print("three" in myDict) #False
print("three" in myDict.values())
print("ten" not in myDict.values())

#len() function, each pair is one element
print(len(myDict))

#all() it's like AND checks 1) if all keys are true
#             2) if all keys are false
#             3) One key is True - False
#             4) One key is False - False
newDict = {
    0: 'zero',
    False: 'False'
}
print(all(newDict))

#any() 1)All keys are True - True
#      2)All keys are False - False
#      3) One key is True - True
#      4) One key is False - True

#sorted() returns a sorted list
print(sorted(myDict))
print(myDict)
