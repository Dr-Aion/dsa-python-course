class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    # the return statement terminates the execution of the function. 
    # Whereas, the yield statement only pauses the execution of the function. 
    # Another difference is return statements are never executed. 
    # whereas, yield statements are executed when the function resumes its execution.
    def __iter__(self, value):
        node = self.head
        while self:
            yield node
            node = node.next
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is not None:
                result += " -> "
        return result
            
    
    # def createDLL(self, value):
    #     new_node = Node(value)
    #     new_node.next = None
    #     new_node.prev = None
    #     self.head = new_node
    #     self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
        self.length += 1
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = None
        self.tail = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next.prev = new_node
        temp_node.next = new_node
        new_node.prev = temp_node
        self.length += 1
    
    def traverse(self):
        if self.head is None:
            return None
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
    
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return current_node
            current_node = current_node.next
        return -1
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return "Index is out of bound"
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node

    def set(self, index, value):
        temp_node = self.get(index)
        temp_node.value = value
        return temp_node

doublyLinkedList = DoublyLinkedList()
# doublyLinkedList.createDLL(5)
print(doublyLinkedList)
doublyLinkedList.prepend(50)
doublyLinkedList.prepend(11)
doublyLinkedList.prepend(14)
doublyLinkedList.append(12)
doublyLinkedList.append(4)
doublyLinkedList.insert(2, 30)
print(doublyLinkedList)
doublyLinkedList.reverse_traverse()
print(doublyLinkedList.search(-30))
print(doublyLinkedList.get(16))
doublyLinkedList.set(4, 67)
print(doublyLinkedList)






