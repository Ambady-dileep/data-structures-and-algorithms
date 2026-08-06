class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def preorder(node):
    if node is None:
        return 
    print(node.value)
    preorder(node.left)
    preorder(node.right)
    
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)
    
    
root = Node("A")
node_b = Node("B")
node_c =  Node("C")
node_d = Node("D")
node_e = Node("E")

root.left = node_b
root.right = node_c

node_b.left = node_d
node_b.right = node_e

print(root.value)
print(root.left.value)
print(root.right.value)
print(root.left.left.value)
print(root.left.right.value)

preorder(root)
inorder(root)
postorder(root)