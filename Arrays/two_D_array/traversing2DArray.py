import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

def traversing2Darray(arr):
    for i in range(len(arr)):                   #O(mn)
        for j in range(len(arr[0])):            #O(n)
            print(arr[i][j])                    #O(1)
traversing2Darray(twoDarray)

#Time Complexity: O(mxn)
#Space Complexity: O(1)