"""
Inorder Successor
Given a node in BST, return the next bigger element

source: https://dxmahata.gitbooks.io/leetcode-python-solutions/content/inorder_successor_in_bst.html
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

def in_order_successor(root, n):
    successor = None
    while root != None and root.data != n.data:
        if root.data > n.data:
            successor = root
            root = root.left
        else:
            root = root.right

    if root == None:
        return None
    
    if root.right == None:
        return successor
    
    root = root.right
    while root.left != None:
        root = root.left
    return root