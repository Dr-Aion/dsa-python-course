class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value) + " "
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return result
            

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

customCLL = CLL()
customCLL.append(6)
customCLL.append(12)
customCLL.append(11)
customCLL.append(7)
customCLL.prepend(100)
customCLL.prepend(4)
print(customCLL)