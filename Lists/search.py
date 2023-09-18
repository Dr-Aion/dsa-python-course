list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#in operator
target = 49
if target in list: #Time Complexity: O(n) under the hood in operator does a linear search
    print(f"{target} is in the list")
else: 
    print(f"{target} is not in the list")

def linear_search(p_list, p_target):
    for i, value in enumerate(list):
        if(value == p_target):
            return i
    return -1
print(linear_search(list, target))
#Time Complexity: O(n)
#Space Complexity: O(1)