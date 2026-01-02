class Node:
    def __init__(self, key):
        self.value = key
        self.left = None 
        self.right = None 

def insert(root, key):
    if root is None: # To check if the first key exists or not if not then we will set the first key 
        return Node(key)
    if root.value == key: # To avoid duplicates 
        return root
    if root.value < key: # If the key is greater, insert into the right subtree
        root.right = insert(root.right, key)
    else: # If the key is smaller, insert into the left subtree
        root.left = insert(root.left, key)
    return root

# 🔷 What Is inorder() Traversal?
# It’s one of the 3 core ways to walk through a binary tree:
# Inorder: Left → Root → Right
# Preorder: Root → Left → Right
# Postorder: Left → Right → Root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")
   
def search(root, key):
    if root is None or root.value == key:
        return root 
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.value:     
        root.left = delete(root.left, key)
    elif key > root.value:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        min_node = find_min(root.right)
        root.value = min_node.value
        root.right = delete(root.right, min_node.value)
    return root

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def get_height(root):
    if root is None:
        return -1  # height of empty tree = -1, or 0 if you prefer nodes count
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def contains(root, key):
    return search(root, key) is not None

def find_closest_value(root, target):
    closest = root.value
    current = root
    while current:
        if abs(target - current.value) < abs(target - closest):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            break  # exact match
    return closest

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.value < max_val):
        return False
    return (
        is_valid_bst(node.left, min_val, node.value) and
        is_valid_bst(node.right, node.value, max_val)
    )



# Build BST
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("Initial Inorder:")
inorder(r)  # Output: 20 30 40 50 60 70 80
print()

# Search test
print("Found 60?", "Yes" if search(r, 60) else "No")  # ✅ Yes
print("Found 100?", "Yes" if search(r, 100) else "No")  # ❌ No

# Delete nodes
r = delete(r, 20)   # leaf
r = delete(r, 30)   # one child
r = delete(r, 50)   # two children

print("Inorder After Deletions (20, 30, 50):")
inorder(r)  # Output: 40 60 70 80
print()

# Search deleted nodes
print("Found 20 after deletion?", "Yes" if search(r, 20) else "No")  # ❌ No
print("Found 30 after deletion?", "Yes" if search(r, 30) else "No")  # ❌ No
print("Found 50 after deletion?", "Yes" if search(r, 50) else "No")  # ❌ No

print("Pre-order:")
preorder(r)
print("\nPost-order:")
postorder(r)
print()

print("Total Nodes:", count_nodes(r)) 
print("Tree Height:", get_height(r)) 
print("Leaf Nodes:", count_leaves(r))

print("Closest to 65:", find_closest_value(r, 65))  # → 60 or 70
print("Closest to 25:", find_closest_value(r, 25))  # → 40

print("Is valid BST?", "Yes" if is_valid_bst(r) else "No")  # ✅ Yes


# 🌳 What is Tree Traversal?
# It’s the process of visiting all nodes of a binary tree in a specific order.

# The 3 main types are:

# Traversal Type	Order
# In-order	Left → Root → Right
# Pre-order	Root → Left → Right
# Post-order	Left → Right → Root

# ✅ Case 3: Delete a node with 2 children ⚠️Important

    #        50
    #      /    \
    #    30      70
    #   /  \    /  \
    # 20   40  60   80
    #               /
    #             75

# In-order successor of 50 = 60 (smallest in right subtree)
# ✅ So:
# Replace 50 with 60
# Then delete 60 from the right subtree

# In-order successor of 30 = 40
# ✅ So:
# Replace 30 with 40
# Delete the node 40 (which is a leaf here)

# 🔁 Summary of Replacements:
# Deleted	Replacement	Notes
# 50	60	Successor in right subtree
# 30	40	Successor in right subtree

    #        60
    #      /    \
    #    40      70
    #   /          \
    # 20           80
    #              /
    #            75
