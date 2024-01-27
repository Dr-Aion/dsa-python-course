class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items if x != None]
        return " ".join(values)
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
                self.items[self.top] = value
    
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                    self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1

customQueue = Queue(8)
print(customQueue.isFull())
customQueue.enqueue(3)
customQueue.enqueue(7)
customQueue.enqueue(2)
customQueue.enqueue(9)
customQueue.dequeue()
print(customQueue.peek())
customQueue.delete()
print(customQueue)

