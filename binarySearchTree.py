# Code for a Binary Search Tree Class + TreeNode Class (Helps Binary Search Tree)

# Class that makes individual Nodes for the Binary Tree
class TreeNode:
    # Sets in root, value, left child, right child, & parent node
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left # Sets left child for the new Node
        self.right_child = right # Sets right child for the new Node
        self.parent = parent # Sets parent node for the new Node
    
    # Inorder iterator of a Binary Tree; Allows use of for i in x syntax
    # Recursive, so it calls onto itself each time to traverse whole tree
    def __iter__(self):
        if self: # If there is a node
        # If node is left child, goes through left subtree & returns elements IF there is still elements
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key # Returns key IF there are still keys
        # If node is right child, goes through right subtree & returns elements IF there is still elements
            if self.right_child:
                for elem in self.right_child:
                    yield elem

    # Determines if node is a left child
    def is_left_child(self):
        # Checks for parent & if the parent's left child is the new Node
        return self.parent and self.parent.left_child is self

    # Determines if node is a right child
    def is_right_child(self):
        # Checks for parent & if the parent's right child is the new Node
        return self.parent and self.parent.right_child is self

    # Determines if node is a root
    def is_root(self):
        # Determines if the Node has a parent or not (NO parent = Root)
        return not self.parent

    # Determines if node is a leaf
    def is_leaf(self):
        # Checks to see if the Node has left or right children
        return not (self.right_child or self.left_child)

    # Determines if node has a child (left/right)
    def has_a_child(self):
        # Checks to see if it has a right/left child
        return self.right_child or self.left_child

    # Determines if a node has both left & right children
    def has_children(self):
        return self.right_child and self.left_child

    # Replaces values in a node
    def replace_value(self, key, value, left, right):
        self.key = key # Key maps to value
        self.value = value
        self.left_child = left
        self.right_child = right
        # Puts new Node on left/right of current child & sets parent to be current node
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    # Finds successor node for the removal of a node w/ two children
    def find_successor(self):
        successor = None
        # If node is a right child, finds min key for right subtree & sets as successor
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            # If node has is a left child of the parent & has no right child, successor is parent of node
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                # Else, node is right child of parent & has no right child --> Successor is successor of parent node
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    # Finds min key in a subtree
    def find_min(self):
        current = self
        # Goes down the left subtree till it hits the left most leaf node
        while current.left_child:
            current = current.left_child
        return current

    # Goes directly to node we want to splice out & makes changes
    def splice_out(self):
        # Checks if node is leaf
        if self.is_leaf():
            # Checks if left/right child & sets it as None (Removal)
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        # Checks if node has a child
        elif self.has_a_child():
            # If node is a left child, sets parent of children of the node to be parent of current node
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                # Else, node is a right child & sets parent of right child of the node to be parent of current node
                else:
                    self.parent.right_child = self.left_child
                # Sets parent of children of current node to be current node's parent
                self.left_child.parent = self.parent
            # Else, node is a right child & sets parent of children of the node to be parent of current node
            else:
                # If child is a left child, sets current node's parent's left child to be that child
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                # Otherwise, child is right child & sets current node's parent's right child to be that child
                else:
                    self.parent.right_child = self.right_child
                # Sets the current node's children to have their parent be current node's parent
                self.right_child.parent = self.parent


class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def size(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # Helper function for put
    def _put(self, key, value, current_node):
        # If key is less than current node's key and there is a left child, it recursively calls itself w/ the left child
        # If there is no left child, a new left child is created by calling TreeNode w/ current node as parent
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        # If key is greater than current node's key and there is a right child, it recursively calls itself w/ the right child
        # If there is no right child, a new right child is created by calling TreeNode w/ current node as parent
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)

    # Puts a node into the tree
    def put(self, key, value):
        # If there is a root, calls helper function to put the value in the Tree
        if self.root:
            self._put(key, value, self.root)
        # If there is no root, creates a new Node to be the root w/ the value
        else:
            self.root = TreeNode(key, value)
        # Keeps track of the size of the Tree
        self.size = self.size + 1

    # Helper function for get
    def _get(self, key, current_node):
        # If current node is nothing (once leaf is reached), return None
        if not current_node:
            return None
        # Returns current node if the key of the current node is key inputted
        if current_node.key == key:
            return current_node
        # If key of current node is greater than inputted key, recursive call to _get on w/ left child
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        # If key of current node is less than inputted key, recursive call to _get w/ right child 
        else:
            return self._get(key, current_node.right_child)

    # Gets a value from a given key
    def get(self, key):
        # If there is a root, key is passed through along w/ root to _get to find if value exists
        if self.root:
            result = self._get(key, self.root)
            # If there is a result, returns the value
            if result:
                return result.value
            # Returns None otherwise
            return None

    # Returns value when inputted in the form of l[key]
    def __getitem__(self, key):
        return self.get(key)

    # Allows use of in operator: Returns True if there is a value; Returns False if None
    def __contains__(self, key):
        return bool(self._get(key, self.root))
    
    # Helper function to delete
    def _delete(self, current_node):
        # Removing a leaf
        if current_node.is_leaf():
            # IF current node is the left child of the parent, left child is removed & set to None
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            # Else, current node is right child of parent & right child is removed & set to None
            else:
                current_node.parent.right_child = None
        # Removing a node with two children
        elif current_node.has_children():
            # Finds successor & cuts out key + value to replace w/ node to be deleted
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        # Removing a node with one child
        else:
            # If current node is a left child, Update parent reference of left child to point to parent of current node
            # Update left child reference of parent to point to current node’s left child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
            # If current node is a right child, Update parent reference of left child to point to parent of current node
            # Update right child reference of parent to point to current node’s left child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
            # If current node has no parent → Root → Replace key, value, left_child, & right_child by calling replace_value method on root
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            # Code for current node if it were a RIGHT CHILD
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    # Deletes a key in a Binary Search Tree
    def delete(self, key):
        # If the size of the tree is greater than one, finds node with key to remove w/ _get
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            # If there is a node w/ the key inputted, calls _delete to remove it & decrements size
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            # Raises an error if there is no node w/ a key in the tree
            else:
                raise KeyError("Error, key not in tree")
        # If tree size is one & root's key is what we're looking for, root is set to None & size is decremented
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        # Otherwise, key is not in tree --> Error
        else:
            raise KeyError("Error, key not in tree")

    # Allows use of del operator (i.e del)
    def __delitem__(self, key):
        self.delete(key)

    # Allows use of dictionary entries l[key] = value
    def __setitem__(self, key, value):
        self.put(key, value)

    # Allows us of in operator
    def __contains__(self, key):
        return bool(self._get(key, self.root))  

my_tree = BinarySearchTree()
my_tree["a"] = "a"
my_tree["q"] = "quick"
my_tree["b"] = "brown"
my_tree["f"] = "fox"
my_tree["j"] = "jumps"
my_tree["o"] = "over"
my_tree["t"] = "the"
my_tree["l"] = "lazy"
my_tree["d"] = "dog"

print(my_tree["q"])
print(my_tree["l"])
print("There are {} items in this tree".format(len(my_tree)))
my_tree.delete("a")
print("There are {} items in this tree".format(len(my_tree)))

for node in my_tree:
    print(my_tree[node], end=" ")
print()