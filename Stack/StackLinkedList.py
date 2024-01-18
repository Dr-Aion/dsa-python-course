class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while(current_node):
            yield current_node
            current_node = current_node.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            values = [str(x.value) for x in self.LinkedList]
            return '\n'.join(values)
        
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        if self.isEmpty():
            new_node = Node(value)
            self.LinkedList.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.LinkedList.head
            self.LinkedList.head = new_node
    
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value
        
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.LinkedList.head.value
        
    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(23)
customStack.push(44)
customStack.push(51)
print(customStack)
print("_________")
customStack.pop()
print("peek " + str(customStack.peek()))
print(customStack)
