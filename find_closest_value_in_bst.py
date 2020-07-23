from basic_data_structures.binary_tree import Node

def find_closest_value_in_bst(tree, target):
    return find_closest_value_helper(tree, target, float("inf"))

def find_closest_value_helper(tree, target, closest):
    """
    >>> test_tree = Node(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
        .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
        .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
        .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
    >>> find_closest_value_in_bst(test_tree, 200)
    203
    """
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(current_node - tree.data):
            closest = current_node.data
        if target < current_node.data:
            current_node = current_node.left
        elif target > current_node.data:
            current_node = current_node.right
        else:
            break
    return closest 

if __name__ == "__main__":
    import doctest
    doctest.testmod()