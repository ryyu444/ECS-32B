# AVL Tree Class - Subclass of BinarySearch Tree

# Makes individual nodes for AVL Tree Class
class AVLTreeNode:
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

class AVLTree:
    
    def _put(self, key, value, current_node):
        # If key is less than current node's key and there is a left child, it recursively calls itself w/ the left child
        # If there is no left child, a new left child is created by calling AVLTreeNode w/ current node as parent
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                # Calls update_balance w/ current node to see if it needs balancing
                self.update_balance(current_node.left_child)
        # If key is greater than current node's key and there is a right child, it recursively calls itself w/ the right child
        # If there is no right child, a new right child is created by calling AVLTreeNode w/ current node as parent
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                # Calls update_balance w/ current node to see if it needs balancing
                self.update_balance(current_node.right_child)

    # Updates balance factors for each node until a value of 0 or the root is reached
    def update_balance(self, node):
        # Checks if current node is out of balance enough to require rebalancing
        # Rebalances node if it is > 1 or < -1; Else, it adjusts balance factor of parent node
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        # If node has a parent, it's balance factor is adjusted if node is already balanced
        if node.parent:
            # If node is a left child, +1 to parent's balance factor
            if node.is_left_child():
                node.parent.balance_factor += 1
            # IF node is a right child, -1 to parent's balance factor
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            # If parent node's balance factor is not 0, recursive call update_balance w/ parent node
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    # Rotates nodes left to balance out tree
    def rotate_left(self, rotation_root):
        # Gets new root to be right child of previous root
        new_root = rotation_root.right_child
        # Replaces right child of old root w/ left child of new root
        rotation_root.right_child = new_root.left_child
        # If new_root has left child --> New Parent of Left Child becomes OLD ROOT
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        # Sets new root's parent to be old root's parent
        new_root.parent = rotation_root.parent
        # If old root was ROOT OF TREE, sets ROOT OF TREE to point to NEW ROOT
        if rotation_root.is_root():
            self._root = new_root
        # If old root is left child, PARENT OF LEFT CHILD changed to POINT TO NEW ROOT
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            # Otherwise, change PARENT of RIGHT CHILD to POINT TO NEW ROOT
            else:
                rotation_root.parent.right_child = new_root
        # Sets new root's left child to be old root
        new_root.left_child = rotation_root
        # Sets old root's parent to be new root
        rotation_root.parent = new_root
        # Calls on balance_factor to rebalance the old & new root's balance factors (Derived in book)
        rotation_root.balance_factor = (
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)
        )

    # Rebalances a Tree to a 0 Balance State
    def rebalance(self, node):
        # If node's balance factor is < 0 (Right Heavy), do a LEFT ROTATION
        if node.balance_factor < 0:
            # If right child's balance factor is > 0 (Left Heavy), do a RIGHT ROTATION FIRST (Check right child first)
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            # Else, right child's balance factor is < 0 (Right Heavy) --> Just do a LEFT ROTATION on node
            else:
                self.rotate_left(node)
        # If node's balance factor > 0 (Left Heavy), do a RIGHT ROTATION (Check left child first)
        elif node.balance_factor > 0:
            # If left child's balance factor < 0 (Right Heavy), do a LEFT ROTATION FIRST
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            # Else, left child's balance factor is > 0 (Left Heavy) --> Just do a RIGHT ROTATION on node
            else:
                self.rotate_right(node)
