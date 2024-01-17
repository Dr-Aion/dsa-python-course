class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        # values = self.list.reverse()
        values = [str(x) for x in self.list]
        values.reverse()
        return "\n".join(values)
    
    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)
        return "the value was pushed"
    
    def pop(self):
        if self.isEmpty():
            return "There are no elements in a Stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There are no elements in a Stack"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None
    
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(11)
customStack.push(3)
customStack.pop()
customStack.pop()
customStack.delete()
print(customStack.peek())
