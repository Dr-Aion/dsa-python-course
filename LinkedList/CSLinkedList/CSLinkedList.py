class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
    
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
                self.tail.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
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

    def search(self, value):
        current = self.head
        while current.next is not None:
            if(current.value == value):
                return True
            current = current.next
            if current is self.head:
                break
        return False
    
    def get(self, index):
        if index < -1 or index > self.length:
            return None
        elif index == -1:
            return self.tail
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        self.head = self.head.next
        self.tail.next = self.head
        popped_node.next = None
        self.length -= 1
        return popped_node
    def pop(self):
        popped_node = self.tail
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        self.tail.next = self.head
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node


            

csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(5)
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.prepend(50)
csLinkedList.prepend(55)
csLinkedList.insert(1, 8)
# csLinkedList.insert(0, 11)
csLinkedList.insert(7, 12)
# print(csLinkedList.tail.value)
# print(csLinkedList)
# csLinkedList.insert(11, 12)
# csLinkedList.traverse()
# print(csLinkedList.search(77))
print(csLinkedList.get(-1))
print(csLinkedList.set(2, 17))
# print(csLinkedList)
print(csLinkedList)
print(csLinkedList.pop_first())
print(csLinkedList)
print(csLinkedList.pop())
print(csLinkedList)
print(csLinkedList.remove(2))
print(csLinkedList)






