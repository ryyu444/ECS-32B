# Ryan Yu
# ECS 032B A04
# 
# Student ID: 919590656

# Problem 3 - Finds last value in a linked list & returns it

# Took Node class from textbook for testing
class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)

def find_last_value(node):
    # Returns None is no nodes exist
    if node is None:
        return None
    # Returns data if next node is None (end of list)
    elif node.next == None: 
        return node.data
    # Recursive call w/ next node if next node is not None
    else:
        return find_last_value(node.next)

# n1 = Node(30)
# n2 = Node(60)
# n3 = Node(30)
# n4 = Node(20)
# n2.set_next(n1)
# n3.set_next(n2)
# n4.set_next(n3)

# print(find_last_value(n3))