class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        length = 0
        temp_node = self.head
        while temp_node:
            length += 1
            temp_node = temp_node.next
        return length
    
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self.tail
