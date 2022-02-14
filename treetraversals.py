# Three Different Tree Traversal Methods
# Difference is WHERE PRINT STATEMENT is/When they go to the ROOT

import operator

# Preorder Tree Traversal
# Root --> Recursive Preorder Traversal of Left Subtree --> Recursive Preorder Traversal of Right Subtree

# Recursive Version
def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

# BinaryTree Method Version
def preorder(self):
    print(self.key)
    if self.left_child:
        self.left_child.preorder()
    if self.right_child:
        self.right_child.preorder()

# Postorder Tree Traversal
# Recursive Postorder Traversal of Left Subtree --> Recursive Postorder Traversal of Right Subtree --> Root Node

# Recursive Version
def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

# Postorder Traversal applied to Parse Trees
def postordereval(tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result_1 = None
    result_2 = None
    if tree:
        # Saves results of Post Order Traversal in results_1 & results_2
        result_1 = postordereval(tree.get_left_child())
        result_2 = postordereval(tree.get_right_child())
        # If there are two results, it does calculation w/ parent node & two results
        if result_1 and result_2:
            return operators[tree.get_root_val()](result_1, result_2)
        else:
            return tree.get_root_val()

# Inorder Tree Traversal
# Recursive Inorder Traversal of Left Subtree --> Root --> Recursive Inorder Traversal of Right Subtree
def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

# Inorder Tree Traversal to get original expression from Parse Tree
def print_exp(tree):
    result = ""
    if tree:
        result = "(" + print_exp(tree.get_left_child())
        result = result + str(tree.get_root_val())
        result = result + print_exp(tree.get_right_child()) + ")"
    return result