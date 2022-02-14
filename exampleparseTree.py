# Example Parse Tree for Mathematical Calculations

import operator

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
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def build_parse_tree(fp_expr): # Fully parenthesized expression
    fp_list = fp_expr.split() # Splits expression
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree) # Pushes parent of expression tree onto stack
    current_tree = expr_tree # Sets current tree to expression tree

    # Goes through each element in fully parenthesized expression
    for i in fp_list:
        
        # Adds new node as left child of root; Pushes parent node onto stack
        # Sets new child to be current node
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child
        
        # Sets root value of current node to operator represented by current token
        # Adds new node as right child of current node; Pushes parent node onto stack
        # Sets new child to be current node
        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child

        # Pops out parent node if token is ")"
        elif i == ")":
            current_tree = p_stack.pop()

    # If element is not an operation, it tries set root value of current node to number & returns to parent
    # Raises an error if it cannot be done
        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                current_tree.root = int(i)
                parent = p_stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return expr_tree

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
# pt.postorder()  # defined and explained in the next section

# Evaluates results from a Parse Tree
def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    # Gets left & right child from current node
    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    # If left & right child are NONE --> Gets operator for current node
    # Applies operators to results from recursively evaluating left & right children [i.e operators["+"](2,2) = operator.add(2,2)]
    if left_child and right_child:
        fn = operators[parse_tree.root] # Operator Module allows values to be calculated
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root # Returns value if left & right child are not NONE
