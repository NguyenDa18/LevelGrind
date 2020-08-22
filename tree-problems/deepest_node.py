"""
Deepest Node in BST
Given a binary tree, find the deepest node in it
Time: O(n) time
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

def find_height(root):
    if (not root):
        return 0
    leftHt = find_height(root.left)
    rightHt = find_height(root.right)
    return max(leftHt, rightHt) + 1

def deepest_node(root, levels):
    """
    >>> root = Node(1)  
    >>> root.left = Node(2)  
    >>> root.right = Node(3)  
    >>> root.left.left = Node(4)  
    >>> root.right.left = Node(5)  
    >>> root.right.right = Node(6)  
    >>> root.right.left.right = Node(7)  
    >>> root.right.right.right = Node(8)  
    >>> root.right.left.right.left = Node(9)  
      
    # Calculating height of tree  
    >>> levels = find_height(root)  
      
    # Printing the deepest node  
    >>> deepest_node(root, levels)
    10
    """
    if (not root):
        return

    if (levels == 1):
        print(root.data)
    elif (levels > 1):
        deepest_node(root.left, levels - 1)
        deepest_node(root.right, levels - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


    