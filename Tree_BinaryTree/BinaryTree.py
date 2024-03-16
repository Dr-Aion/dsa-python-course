import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee 
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
# preOrderTraversal(newBT)

def inOrderTravelsal(rootNode):
    if not rootNode:
        return
    inOrderTravelsal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTravelsal(rootNode.rightChild)
# inOrderTravelsal(newBT)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
# postOrderTraversal(newBT)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
# levelOrderTraversal(newBT)
                
def searchBinaryTree(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "the node exists"
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)    
        return "the node doesn't exist"
print(searchBinaryTree(newBT, "Caramel"))