class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        values.reverse()
        return '\n'.join(values)
    
    def isEmpty(self):
        if not self:
            return True
        else:
            return False
        
    def isFull(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            if(len(self.list) == self.maxSize):
                return True
            else:
                return False

    def push(self, value):
        if self.isFull():
            return "The Stack is full"
        else:
            self.list.append(value)
            return "The element is pushed"
    
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list[len(self.list) - 1]
    
    def delete(self):
        self.list = None

customStack = Stack(5)
customStack.push(45)
customStack.push(55)
customStack.push(22)
customStack.push(11)
customStack.push(33)
customStack.push(73)
print(customStack)
print(customStack.isFull())
print(customStack)
print("pop " + str(customStack.pop()))
print("peek " + str(customStack.peek()))




