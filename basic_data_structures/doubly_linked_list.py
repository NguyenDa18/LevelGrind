# reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/linked_list/doubly_linked_list.py

"""
Doubly Linked List
 next <-> prev 
el <-> head <-> tail
"""

class LinkedList:
    """
    >>> empty_list = LinkedList()
    >>> empty_list.isEmpty()
    >>> True
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insertHead(self, val):
        newLink = Link(val)
        if self.isEmpty():
            self.tail = newLink
        else:
            self.head.previous = newLink

        newLink.next = self.head
        self.head = newLink

    def deleteHead(self):
        headToDelete = self.head
        self.head = self.head.next
        self.head.previous = None
        if self.head is None:
            self.tail = None
        return headToDelete

if __name__ == "__main__":
    import doctest
    doctest.testmod()