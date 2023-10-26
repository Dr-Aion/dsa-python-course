class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def insert(self, index, value):
        if index > self.length or index < 0:
            raise Exception("index out of range")
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = self.head
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traverse(self):
        current = self.head
        while current.next is not None:
            print(current.value)
            current = current.next
            if current is self.head:
                break
            

csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(5)
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.prepend(50)
csLinkedList.prepend(1)
csLinkedList.insert(1, 8)
csLinkedList.insert(0, 11)
csLinkedList.insert(8, 12)
print(csLinkedList.tail.value)

print(csLinkedList)
# csLinkedList.insert(11, 12)
csLinkedList.traverse()
