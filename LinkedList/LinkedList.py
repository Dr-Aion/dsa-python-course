class Node:
    def _init_(self, value):
        self.value = value;
        self.next = None;

class LinkedList:
    def _init_(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list.lenght)