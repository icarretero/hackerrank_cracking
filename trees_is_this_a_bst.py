""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def is_BST(node, parent_value):
    if node.left:
        if node.left.data >= node.data or not is_BST(node.left):
              return False
    if node.right:
        if node.right.data <= node.data or not is_BST(node.right):
            return False
    return True

def checkBST(root):
    return is_BST(root, root.data)
