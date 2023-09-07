import array as arr
#Time Complexity: O(1)
#Space Complexity: O(1)
my_array = arr.array('i') #typecode: i - signed integer
print(my_array)
#Time Complexity: O(n)
#Space Complexity: O(n)
my_array1 = arr.array('i', [1, 2, 4]) #typecode: i - signed integer
print(my_array1)

def traverseArray(array):
    for i in array:
        print(i)
traverseArray(my_array1)

import numpy as np
#Time Complexity: O(1)
#Space Complexity: O(1)
np_array = np.array([], dtype = int)
print(np_array)
#Time Complexity: O(n)
#Space Complexity: O(n)
np_array1 = np.array([1, 2, 3, 4])
print(np_array1)


