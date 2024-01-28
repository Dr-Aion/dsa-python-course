class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def insert(self, index, value):
        if index < 0 and index > self.length:
            return False
        elif self.isEmpty():
            self.prepend(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def search(self, target):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if(temp_node.value == target):
                return index
            else:
                temp_node = temp_node.next
                index += 1
        return "This node doesn't exitst"




    
customLinkedList = LinkedList()
customLinkedList.prepend(7)
customLinkedList.prepend(12)
customLinkedList.prepend(9)
customLinkedList.prepend(2)
customLinkedList.prepend(3)
customLinkedList.insert(3, 55)
print(customLinkedList.search(23))

print(customLinkedList)

