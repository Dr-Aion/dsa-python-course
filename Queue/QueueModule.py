from collections import deque

customQueue = deque(maxlen = 3)
customQueue.append(5)
customQueue.append(11)
customQueue.append(50)
customQueue.append(45)
print(customQueue.popleft())
print(customQueue)
customQueue.clear()
print(customQueue)