# Ryan Yu
# ECS 032B A04
# 
# Student ID: 919590656

# Problem 2 - Determines where a given data value is in a linked list

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

def find_value(value, node):
    if node == None: # Returns False if node is None
        return False
    else:
        if node.data == value: # Returns True if data in node == value
            return True
        else:
            return find_value(value,node.next) # Recursive call w/ next node otherwise

# n1 = Node(10)
# n2 = Node(60)
# n3 = Node(30)
# n4 = Node(20)
# n2.set_next(n1)
# n3.set_next(n2)
# n4.set_next(n3)

# print(find_value(50,n4))