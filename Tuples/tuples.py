newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple2 = ('a',) #a tuple with one element, don't forget the comma, otherwise python will treat it as a string
print(newTuple)

#creating a tuple using a built-in tuple function
newTuple3 = tuple() #an empty tuple
print(newTuple3)

newTuple4 = tuple('abcde') #the result of this function will be atuple with the elements of sequence
print(newTuple4)

#Time Complexity: O(1)
#Space Complexity: O(n)