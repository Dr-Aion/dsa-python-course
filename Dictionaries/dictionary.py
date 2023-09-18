#a dict() constructor
#Time Complexity = O(1)
#Space Complexity = O(1)
myDict = dict()
print(myDict)

myDict2 = {}
print(myDict2)


#Time Complexity = O(n)
#Space Complexity = O(n)
engSp = dict(one = 'uno', two = 'dos', three = 'tres')
print(engSp)

engSp2 = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'}
print(engSp2)

engSp3_list = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
engSp3 = dict(engSp3_list)
print(engSp3)

