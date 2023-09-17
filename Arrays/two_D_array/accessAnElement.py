import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

def accessElement(arr, rowIndex, colIndex):
    if(rowIndex >= len(arr) or colIndex >= len(arr[0])):  #O(1)
        print("Incorrect Index")                          #O(1)
    else:
        print(arr[rowIndex][colIndex])                    #O(1)
accessElement(twoDarray, 1, 2)
accessElement(twoDarray, 0, 3)

#Time Complexity: O(1)
#Space Complexity: O(1)