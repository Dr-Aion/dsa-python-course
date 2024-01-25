class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        print(" ".join(values))
    
    def isFull(self):
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
customQueue = Queue(8)
print(customQueue.isFull())
