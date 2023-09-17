import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

def linearSearch(arr, value):
    for i in range(len(arr)):                                                                    #O(mn)
        for j in range(len(arr[0])):                                                             #O(n)
            if(arr[i][j] == value):                                                             
                return "the value is at index[" + str(i) + "]" + "[" + str(j) + "]in the array"  #O(1)
    return "the value isn't found in the array"
print(linearSearch(twoDarray, 17))

#Time Complexity O(mn)
#Space Complexity O(1)