# Contains examples of trees

# Standard 3 Height Tree
my_tree = [
    "a",  # root
        ["b",  # left subtree
            ["d", [], []],
            ["e", [], []]
        ],
        ["c",  # right subtree
            ["f", [], []],
            []
        ],
    ]

# my_tree = ["a", ["b", ["d", [], []], ["e", [], []]], ["c", ["f", [], []], []]]
# print(my_tree)
# print("left subtree = ", my_tree[1])
# print("root = ", my_tree[0])
# print("right subtree = ", my_tree[2])

# Code for making a Binary Tree + Inserting Elements to Left or Right Subtrees

# Makes the binary tree
def make_binary_tree(root):
    return [root, [], []]

# Inserts a child to the left of the root
def insert_left(root, new_child):
    # Pops left subtree
    old_child = root.pop(1)
    # Inserts new child to old_child place & moves old_child to be child of new one
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []]) # [] is the "second" child w/ None because no input
    else:
        # Creates left subtree & inserts two Nones b.c there is no left child
        root.insert(1, [new_child, [], []])
    return root # Start of tree returned

# Inserts a child to the right of the root
def insert_right(root, new_child):
    # Pops right subtree
    old_child = root.pop(2)
    # Inserts new child to old_child place & moves old_child to be child of new one
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child]) # [] is the "second" child w/ None because no input
    else:
        # Creates right subtree & inserts two Nones b.c there is no right child
        root.insert(2, [new_child, [], []])
    return root # Returns start of tree

# Gets root value
def get_root_val(root):
    return root[0]

# Sets root value
def set_root_val(root, new_value):
    root[0] = new_value

# Gets left subtree
def get_left_child(root):
    return root[1]

# Gets right subtree
def get_right_child(root):
    return root[2]


a_tree = make_binary_tree(3)
insert_left(a_tree, 4)
insert_left(a_tree, 5)
insert_right(a_tree, 6)
insert_right(a_tree, 7)
left_child = get_left_child(a_tree)
print(left_child)

set_root_val(left_child, 9)
print(a_tree)
insert_left(left_child, 11)
print(a_tree)
print(get_right_child(get_right_child(a_tree)))