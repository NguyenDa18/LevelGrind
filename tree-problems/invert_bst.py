"""
Invert Binary Tree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
def invert(tree):
    """
    >>> root = Node(2)
    >>> root.left = Node(1)
    >>> root.right = Node(4)
    >>> root.right.left = Node(3)
    >>> root.right.right = Node(5)
    >>> invert(root)
    >>> print_tree(root)
    5
    4
    3
    2
    1
    """
    if tree == None:
        return
    else:
        invert(tree.left)
        invert(tree.right)

        # swap
        tree.left, tree.right = tree.right, tree.left

def print_tree(tree):
    if tree == None:
        return
    print_tree(tree.left)
    print(tree.data)
    print_tree(tree.right)

def post_order_traverse(tree):
    """
    >>> root = Node(2)
    >>> root.left = Node(1)
    >>> root.right = Node(4)
    >>> root.right.left = Node(3)
    >>> root.right.right = Node(5)
    >>> invert(root)
    >>> post_order_traverse(root)
    5
    3
    4
    1
    2
    """
    if tree == None:
        return
    
    post_order_traverse(tree.left)
    post_order_traverse(tree.right)
    print(tree.data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()