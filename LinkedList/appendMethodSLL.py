class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 and index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False
    
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(40)
new_LinkedList.prepend(5)
new_LinkedList.insert(1, 50)
new_LinkedList.insert(-2, 35)
print(new_LinkedList.search(40))

# print(new_LinkedList.head.value)
# print(new_LinkedList.tail.value)
# print(new_LinkedList.length)
# print(new_LinkedList)
new_LinkedList.traverse()

