#Creates a new 2Darray without the row or column

import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])
new2DArray = np.delete(twoDarray, 0, 1)
print(new2DArray)


#Time Complexity: O(mn)
#Space Complexity: O(mn)