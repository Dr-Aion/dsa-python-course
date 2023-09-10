from array import *
arr = array('i', [4, 2, 3, 8, 7])

def accessElement(array, index):
    if(index >= len(array)):
        print("There's no element at index "+ str(index))
    else:
        print(array[index])
accessElement(arr, 5)

#Time Complexity: O(1)
#Space Complexity: O(1)