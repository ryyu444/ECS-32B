# Ryan Yu
# ECS 032B A04
# 
# Student ID: 919590656

# Problem 1 - Finding largest integer in a list

def find_largest(l):
    # Returns None if list is empty
    if len(l) == 0:
        return None
    # Returns item if list has one element
    if len(l) == 1:
        return l[0]
    # Recursive calls w/ a list slice
    else:
        end_index = len(l) - 1 # Gets last element index of list
        # Compares first element to last; If last is greater, first element is sliced out; Else, last is cut out
        if l[0] < l[end_index]:
            return find_largest(l[1:]) 
        else:
            return find_largest(l[:end_index])
