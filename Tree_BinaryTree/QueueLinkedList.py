class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.queue.head is None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.queue.head = newNode
            self.queue.tail = newNode
        else:
            self.queue.tail.next = newNode
            self.queue.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            firstNode = self.queue.head
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return firstNode
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.queue.head
        
    def delete(self):
        self.queue.head = None
        self.queue.tail = None
        
# customQueue = Queue()
# customQueue.enqueue(3)
# customQueue.enqueue(8)
# customQueue.enqueue(10)
# customQueue.enqueue(44)
# print(customQueue.dequeue())
# print(customQueue.peek())
# customQueue.delete()
# print(customQueue)