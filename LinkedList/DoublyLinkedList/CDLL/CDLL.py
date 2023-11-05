class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        print(self.value)

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            temp_node = temp_node.next
            if temp_node == self.tail.next:
                break
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.tail.next:
                break
            result += " -> "
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = new_node
            self.tail.next = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
            self.length += 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = new_node
            self.tail.next = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            self.length += 1

    def insert(self, index, value):
        if index < -1 or index >= self.length:
            return "index is out of bound"
        elif index == 0:
            self.prepend(value)
        elif index == -1 or index == self.length - 1:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            new_node.next.prev = new_node
            temp_node.next = new_node
        

circularDoublyLinkedList = CircularDoublyLinkedList()
circularDoublyLinkedList.prepend(5)
circularDoublyLinkedList.prepend(15)
circularDoublyLinkedList.prepend(20)
circularDoublyLinkedList.append(11)
circularDoublyLinkedList.append(12)
circularDoublyLinkedList.insert(1, 30)



print([node.value for node in circularDoublyLinkedList])
print(circularDoublyLinkedList)
print(circularDoublyLinkedList.head.prev.value)

