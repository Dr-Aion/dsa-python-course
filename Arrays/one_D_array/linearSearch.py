from array import *
arr = array('i', [2, 8, 4, 1, 9, 0])

def linearSearch(array, target):
    for i in range (len(array)):
        if(array[i] == target):
            return i
    return -1
print(linearSearch(arr,11))