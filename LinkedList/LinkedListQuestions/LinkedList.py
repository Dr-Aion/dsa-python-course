import random
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

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(random.randint(min_value, max_value))
        return self

    def remove_duplicates(ll):
        if ll.head is None:
            return
        current_node = ll.head
        prev_node = None
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
 
        ll.tail = prev_node  
        return ll.head
    def nthToLast(ll, n):
        pointer1 = ll.head
        pointer2 = ll.head

        for i in range(n):
            if pointer2 is None:
                return None
            pointer2 = pointer2.next

        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
    
customLinkedList = LinkedList()
customLinkedList.generate(5, 1, 10)
print(customLinkedList)
print(len(customLinkedList))

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))