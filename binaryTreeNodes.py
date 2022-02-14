# Code for a Binary Tree w/ Nodes & References

class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj # Sets self.key = Root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        # Creates new left child Node if there is no existing left child
        #  new_node becomes root due to instance calling
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        # Creates new left child Node, sets new left child's left child to be current left child, & sets current left child to be new Node
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        # Creates new right child Node if there is no existing right child
        #  new_node becomes root due to instance calling
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
                # Creates new right child Node, sets new right child's right child to be current right child, & sets current right child to be new Node
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    # Returns root value
    def get_root_val(self):
        return self.key

    # Sets root value
    def set_root_val(self, new_obj):
        self.key = new_obj

    # Gets left child
    def get_left_child(self):
        return self.left_child

    # Gets right child
    def get_right_child(self):
        return self.right_child


a_tree = BinaryTree("a")
print(a_tree.get_root_val())
print(a_tree.get_left_child())
a_tree.insert_left("b")
print(a_tree.get_left_child())
print(a_tree.get_left_child().get_root_val())
a_tree.insert_right("c")
print(a_tree.get_right_child())
print(a_tree.get_right_child().get_root_val())
a_tree.get_right_child().set_root_val("hello")
print(a_tree.get_right_child().get_root_val())
