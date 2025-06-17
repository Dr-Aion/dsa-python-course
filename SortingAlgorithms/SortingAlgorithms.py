import math
def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList) - i - 1):
            if(customList[j] > customList[j + 1]):
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)

customList = [5, 7, 4, 3, 8, 6, 1, 9, 2]
# bubbleSort(customList)

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)): 
            if(customList[min_index] > customList[j]):
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)
customList = [5, 7, 4, 3, 8, 6, 1, 9, 2]
# selectionSort(customList)

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while(j >= 0 and key < customList[j]):
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return (customList)
customList = [5, 7, 4, 3, 8, 6, 1, 9, 2]
# insertionSort(customList)

def bucketSort(customList):
    numOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numOfBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numOfBuckets/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(numOfBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return (customList)

print(bucketSort(customList))
bucketSort(customList)
