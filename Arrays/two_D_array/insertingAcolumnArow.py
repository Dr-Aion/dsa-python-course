import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

newTwoDArray = np.insert(twoDarray, 0, [[1, 2, 3, 4]], axis = 1) #0 - first column;  axis: 0 - row, 1 - column
newTwoDArray = np.insert(newTwoDArray, 2, [[11, 12, 13, 14, 15]], axis = 0) #0 - first column;  axis: 0 - row, 1 - column
newTwoDArray = np.append(newTwoDArray, [[21, 22, 23, 24, 25]], axis = 0) # append adds a row or column at the end of the array


print(newTwoDArray)