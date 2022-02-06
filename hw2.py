# Ryan Yu
# ECS 032B A04

# Student ID: 919590656

# Modified to include a reference to previous node for Deque2()

class Node: # Provided by Textbook (Needed to run UnorderedList, Stack, & Queue)
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None
        self._prev = None

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

    def get_prev(self): # Gets previous node
        return self._prev

    def set_prev(self, node_prev): # Sets previous node
        self._prev = node_prev

    prev = property(get_prev, set_prev)

    def __str__(self):
        """String"""
        return str(self._data)

# Problem 1 - Creates a queue where front is the start of list & rear is end of list

class QueueX(): 

    def __init__(self):
        self.items = []

    # Checks to see if queue is empty
    def is_empty(self):
        return self.items == []

    # Inserts item into queue from end of list (or adds an item if it is empty)
    def enqueue(self,item):
        if len(self.items) > 0:
            self.items.insert(len(self.items),item)
        else:
            self.items.append(item)

    # Removes front most item from queue
    def dequeue(self):
        return self.items.pop(0)

    # Returns length of queue
    def size(self):
        return len(self.items)

# Problems 2, 3, & 4
# Modifies code provided by Textbook to include append(), index(), pop(), insert(), slice(), & convert() 

class UnorderedList:

    def __init__(self): # Sets head of Unordered Linked List to None
        self.head = None

    def is_empty(self): # Checks to see if linked list is empty
        return self.head == None

    def add(self, item): # Adds an item to a linked list
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self): # Goes through number of nodes & returns length of linked list
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count
    
    def search(self, item): # Goes through data within nodes & checks to see if item is in list
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        
        return False

    def remove(self, item): # Removes a node based on the item entered
        current = self.head
        previous = None
    # Goes through data in each node & keeps track of node before current
    # If data in node matches item to be removed, loop is exited
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        
    # Returns an error if the end of list is reached & item is not found
        if current is None:
            raise ValueError("{} is not in the list".format(item))
    
    # If item is found in first node, it sets the new starting node to be the next node
    # Otherwise, it sets the previous node to refer to the node after the current as the next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        
    def append(self, item): # Adds a node to the end of a list based on item entered
        current = self.head
        prior = None
        # Goes through each node till end of list is reached
        while current is not None:
            prior = current
            current = current.next
        # Creates a new node at end of list & makes previous ending node refer to it
        if current == None and prior == None:
            newItem = Node(item)
            newItem.set_next(None)
            self.head = newItem
        if current == None and prior != None:
            newItem = Node(item)
            newItem.set_next(None)
            prior.next = newItem

    def index(self, item): # Tries to find an index in the list for item entered
        current = self.head
        position = 0
    # Goes through data of each node while keeping track of position
    # Returns position if data matches item
        while current is not None:
            if current.data == item:
                return position
            position = position + 1
            current = current.next

    def insert(self, position, item): # Inserts a node w/ item in position of list entered
        current = self.head
        index = 0
        previous = None
    # Inserts a new node at the position specified by keeping track of the index of the list
    # Sets the previous node to refer to the new node & new node to refer to the current node
        while current is not None:
            if position == 0:
                newItem = Node(item)
                newItem.set_next(current)
                self.head = newItem
                break
            if index == position:
                newItem = Node(item)
                newItem.set_next(current)
                previous.next = newItem
                break
            index = index + 1
            previous = current
            current = current.next
    # If position is at the end of the list, previous end node is set to refer to new node & new node refers to None
        if position == index and current is None:
            newItem = Node(item)
            newItem.set_next(None)
            previous.next = newItem

    def pop(self, position = -1): # Removes a node from a specified position of a list
        current = self.head
        prior = None
        pre_prior = None
        index = 0
    
    # Keeps track of index within list; Checks to see if index is same as position inputted
    # If position is the same, current data value is returned & previous node is set to refer to the node after current
        while current is not None:
            if position == 0:
                self.head = current.next
                return current        
            if position == index:
                prior.next = current.next
                return current.data
            if prior is not None:
                pre_prior = prior    
            prior = current
            current = current.next
            index = index + 1
                
        if current is None and position == -1:
            pre_prior.next = prior.next
            return prior

    def slice(self, start, stop): # Returns specific values of a list from two positions
        current = self.head
        listslice = UnorderedList()
        pos = 0
    # Goes through nodes until start point is reached; Node data is appended up to the node before stop
    # List slice is returned
        while current is not None:
            if pos >= start and pos < stop:
                listslice.append(current.data)
            pos = pos + 1
            current = current.next

        return listslice

    def convert(self): # Turns a linked list into a default Python List
        current = self.head
        PythonList = []
    # Goes through each node and appends the data to a default Python List; Returns the list
        while current is not None:
            PythonList.append(current.data)
            current = current.next
        
        return PythonList

    #  def pop(self): # Removes a node from the end of a list
    #     current = self.head
    #     prior = None
    #     pre_prior = None
    # # Keeps track of current node, the node before it, and the node after until end of list
    #     while current is not None:
    #         if prior is not None:
    #             pre_prior = prior
    #         prior = current
    #         current = current.next
    # # At end of list, the node before the end will refer to None & the node before that will refer to it
    # # Returns the previous end node data
    #     if current == None:
    #         pre_prior.next = prior.next
    #         return prior.data

# Problem 5 - Create a stack w/ linked lists

class Stack:

    def __init__(self):
        self.head = None

    def push(self, item): # Adds a new item to top (end) of stack
        current = self.head
        previous = None
    # Goes through each node
        while current is not None:
            previous = current
            current = current.next
    # If the previous node is None (Start of list), a new node is added and set to be the head
    # It points to None because it is the only entry in the list    
        if previous == None:
            newNode = Node(item)
            newNode.set_next(None)
            self.head = newNode
    # If there is a previous node & current is None (End of list), a new node is added to the top
    # The previous node is then set to refer to the new node
        if current == None and previous != None:
            newNode = Node(item)
            newNode.set_next(None)
            previous.next = newNode

    def pop(self): # Removes top item from stack & returns it
        current = self.head
        previous = None
        pre_previous = None
    # Goes through each node until the end is reached & keeps track of previous node, the node before that, & the current node
        while current is not None: 
            if previous is not None:
                pre_previous = previous
            previous = current
            current = current.next
    # Once the end is reached, the last node's data is returned & the second node before the last is set to refer to the new end node 
        if current == None:
            pre_previous.next = previous.next
            return previous.data

    def peek(self): # Looks at top of list & returns the value
        current = self.head
        previous = None
    # Iterates through each node till it reaches the end & keeps the previous node stored
        while current is not None:
            previous = current
            current = current.next
    # Once the end is reached, the last node of the list's data is returned    
        if current == None:
            return previous.data

    def is_empty(self): # Checks to see if stack is empty; Returns Boolean
    #     current = self.head
    #     previous = None
    # # Goes through each node of the list till the end
    #     while current is not None:
    #         previous = current
    #         current = current.next
    # # If the end refers to None and the previous "node" refers to None, it must be empty --> True
    #     if current == None and previous == None:
    #         return True
    # # If the end refers to None and the previous node refers to something, there must be contents
    #     if current == None and previous != None:
    #         return False
        
        if self.head == None:
            return True

    def size(self): # Returns number of items in stack
        current = self.head
        count = 0
    # Goes through each node in the list till the end & counts number of nodes
        while current is not None:
            current = current.next
            count = count + 1
    # Returns count of nodes after reaching the end
        if current == None:
            return count

# Problem 6 - Create a queue w/ linked lists

class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, item): # Adds a new item to rear (end of list) of queue
        current = self.head
        previous = None
    # Goes through each node until end of list is reached
        while current is not None:
            previous = current
            current = current.next
    # If previous equals none (start of list), a new node is created and is referred to by the head
        if previous == None:
            newNode = Node(item)
            newNode.set_next(None)
            self.head = newNode
    # If end of list is reached & previous references something, the node is created and the previous node is set to refer to it
        if current == None and previous != None:
            newNode = Node(item)
            newNode.set_next(None)
            previous.next = newNode

    def dequeue(self): # Removes from item from queue
        # Sets current to be head, the head to refer to the next node, and returns current data
        current = self.head
        if current.next == None:
            self.head = None
            return current
        else:
            self.head = current.next
            return current.data

    def is_empty(self): # Checks to see if queue is empty
    #     current = self.head
    #     previous = None
    # # Goes through each node in list until the end of the list
    #     while current is not None:
    #         previous = current
    #         current = current.next
    # # If the end refers to None & the previous node also refers to None, it must be empty --> True
    #     if current == None and previous == None:
    #         return True
    # # If the end refers to None & the previous node refers to something other than None, it must have contents --> False    
    #     if current == None and previous != None:
    #         return False

        if self.head == None:
            return True

    def size(self): # Returns number of items in queue
        current = self.head
        count = 0
    # Goes through each node and keeps count of nodes until end of list
        while current is not None:
            current = current.next
            count = count + 1
    # At end of list, count of nodes is returned
        if current == None:
            return count    

# Problem 7 - Create a doubly linked list

class Deque2():

    def __init__(self): # Sets head and tail to be None
        self.head = None
        self.tail = None

    # def print_list(self): # Print debugging
    #     node = self.head
    #     while node != None:
    #         print(node.data)
    #         node = node.next
            
    def add_front(self, item): # Adds new item to front of deque
    # Creates a new Node if list is empty; Sets next reference to None; Sets head & tail to Node
        if self.head == None:
            newNode = Node(item)
            newNode.set_next(None)
            self.head = newNode
            self.tail = newNode

    # Creates a new Node at front of list & sets next reference to previous head; Then sets head to new Node
        else:
            newNode = Node(item)
            self.head.prev = newNode
            newNode.set_next(self.head)
            newNode.set_prev(None)
            self.head = newNode
        
    def add_rear(self, item): # Adds new item to end of deque
    # Creates a new Node if list is empty; Sets next reference to None; Sets head & tail to Node
        if self.head == None:
            newNode = Node(item)
            newNode.set_next(None)
            self.tail = newNode
            self.head = newNode
    
    # Creates a new Node at end of list & sets next reference to None;
    # Sets previous reference for the newNode to the previous tail; Then sets tail to new Node
        else:
            newNode = Node(item)
            self.tail.next = newNode
            newNode.set_next(None)
            newNode.set_prev(self.tail)
            self.tail = newNode

    def remove_front(self): # Removes front item from deque

        if self.head == None: # Returns None if there are no nodes in list
            return None

    # If head = tail, there must be one entry
    # Head & Tail are set to none b.c only entry is removed --> Node's data is returned
        if self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            return current
        
    # If the head's next reference is the tail, there are only two entries
    # Head is set to tail + head's previous reference is set to None + Current head data returned
    # Head is set to tail because there is only one entry after removed
        if self.head.next == self.tail:
            current = self.head
            self.head = self.tail
            self.head.prev = None

            return current
        
    # Stores current head in current & returns the data in the node
    # Sets new head to be next node + Sets new head's previous reference to None
        else:
            current = self.head
            self.head = current.next
            current_head = self.head
            current_head.prev = None
        
            return current.data

    def remove_rear(self): # Removes last item from deque
    # Sets current to tail & updates it so the tail is the node before it
    # Changes next reference of new tail to None; Returns tail data
    
    # Method 1: Iterate till end of list & set tail
        # current = self.head
        # previous = None
        # prior = None

        # while current is not None:
        #     if previous is not None:
        #         prior = previous
        #     previous = current
        #     current = current.next
        
        # if self.head == None:
        #     return self.head
        
        # if current == None and prior == None:
        #     previous = self.tail
        #     self.tail = None
        #     self.head = None
        #     return previous

        # else:
        #     prior.next = None
        #     self.tail = prior

        # return previous

    # Method 2: Sets tail to be previous node and sets that prev node's next reference to None
        
        if self.tail == None: # Returns None if there are no nodes in list
            return None
        
    # If head = tail, there must be one entry
    # Head & Tail are set to none b.c only entry is removed --> Node's data is returned
        if self.head == self.tail:
            current = self.tail
            self.head = None
            self.tail = None
            return current

    # If the head's next reference is the tail, there are only two entries
    # Tail is set to head + tail's next reference is set to None + Current tail data returned
    # Tail is set to head because there is only one entry after removed
        if self.head.next == self.tail:
            current = self.tail
            self.tail = self.head
            self.tail.next = None

            return current

    # Stores current tail in current & returns the data in the node
    # Sets new tail to be previous node + Sets new tail's next reference to None
        else:
            current = self.tail
            self.tail = current.prev
            current_tail = self.tail
            current_tail.next = None
        
            return current.data

    def is_empty(self): # Checks to see if list is empty
    # Method 1: Traversal through list to check if list is empty
        # current_head = self.head
        # previous_head = None
        
        # while current_head is not None:
        #     previous_head = current_head
        #     current_head = current_head.next

        # if previous_head == None and current_head == None:
        #     return True
        
        # if previous_head != None and current_head == None:
        #     return False
    
    # Method 2: Checks to see if head refers to any node & returns Boolean
        return self.head == None

    def size(self): # Returns size of list
        current = self.head
        counter = 0
    
    # Goes through each node until end of list is reached & increments a counter
        while current is not None:
            current = current.next
            counter = counter + 1
    
    # Returns counter once end of list is reached
        if current == None:
            return counter



