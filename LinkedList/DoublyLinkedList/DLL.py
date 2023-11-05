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
        if self.tail is None:
            return None
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev
    def search(self, value):
        if self.head is None:
            return None
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return temp_node
                temp_node = temp_node.next
            return -1
    
    def delete(self, index):
        if self.head is None:
            return None
        if index == 0:
            deleted_node = self.head
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = deleted_node.next
                self.head.prev = None
                deleted_node.next = None
            return deleted_node
        elif index == -1 or index == self.length - 1:
            deleted_node = self.tail
            if self.tail.prev is None:
                self.head = None
                self.tail = None
            else:
                self.tail = deleted_node.prev
                self.tail.next = None
                deleted_node.prev = None
            return deleted_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            deleted_node = temp_node.next
            temp_node.next = deleted_node.next
            deleted_node.next.prev = temp_node
            deleted_node.prev = None
            deleted_node.next = None
            return deleted_node

    def delete_all(self):
        if self.head is None:
            return None
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None

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
# doublyLinkedList.reverse_traverse()
# print(doublyLinkedList.search(13))
print(doublyLinkedList.delete(0))
print(doublyLinkedList.delete(-1))
print(doublyLinkedList.delete(2))
print(doublyLinkedList)
doublyLinkedList.delete_all()
print(doublyLinkedList)




