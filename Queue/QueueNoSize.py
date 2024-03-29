class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        if self.isEmpty():
            return "Queue is empty"
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False
    
    # Time complexity: Amortized time O(1), in worst case scenario O(n) or even O(n^2)
    def enqueue(self, value): 
        self.items.append(value)
        return "The element has been enqueued into the Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
        

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(3)
customQueue.enqueue(5)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)