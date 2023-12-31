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
        index = 0
        while current:
            if current.value == target:
                return True, index
            current = current.next
            index = index + 1
        return False
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.tail = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    def pop(self):
        if self.length == 0:
            return None
        popped_last = self.tail
        if self.length == 1:
            self.tail = None
            self.tail = None
            return popped_last
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_last.value
    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop()
        prev = self.get(index - 1)
        popped_node = prev.next
        prev.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
 
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(40)
new_LinkedList.prepend(5)
new_LinkedList.insert(1, 50)
new_LinkedList.insert(-2, 35)
print(new_LinkedList.search(40))
print(new_LinkedList.get(6))
print(new_LinkedList.set_value(1, 100))
print(new_LinkedList)
print(new_LinkedList.pop_first())
print(new_LinkedList)
print(new_LinkedList.pop())
print(new_LinkedList)
print(new_LinkedList.remove(2))
print(new_LinkedList)







# print(new_LinkedList.head.value)
# print(new_LinkedList.tail.value)
# print(new_LinkedList.length)
# print(new_LinkedList)
# new_LinkedList.traverse()

