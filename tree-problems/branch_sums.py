class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        return self

def branch_sums(root):
    """
    >>> test_tree = Node(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
    >>> branch_sums(test_tree)
    [108, 125, 142]
    """
    sums = []
    branch_sums_helper(root, root.data, sums)
    return sums

def branch_sums_helper(root, runningSum, sums):
    if not root.left and not root.right:
        sums.append(runningSum)
        return

    if root.left:
        runningSum += root.left.data
        branch_sums_helper(root.left, runningSum, sums)
        runningSum -= root.left.data

    if root.right:
        runningSum += root.right.data
        branch_sums_helper(root.right, runningSum, sums)
        runningSum -= root.right.data

if __name__ == "__main__":
    import doctest
    doctest.testmod()