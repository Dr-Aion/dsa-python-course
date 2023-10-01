class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;

new_node = Node(10)
print(new_node.value)

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#empty LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

newLinkedList = LinkedList()
print(newLinkedList.length)


    