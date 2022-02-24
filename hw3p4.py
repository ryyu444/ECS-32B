# Ryan Yu
# ECS 032B A04
# 
# Student ID: 919590656

# Problem 4 - Modification to binarySearchRec(alist,item) to perform a ternary search on a Python List

def ternarySearchRec(l, item):
    if len(l) == 0: # Returns False if list is empty
        return False
    elif len(l) == 1: # Checks item in list when list has one element --> Returns True/False
        return l[0] == item
    elif len(l) == 2: # Checks two items in list when list has two elements --> Returns True if either are item; False otherwise
        if l[0] == item or l[1] == item:
            return True
        else:
            return False
    else:
        # Calculates midpoints for list
        first_mid = len(l) // 3 
        second_mid = len(l) - first_mid
        # Checks to see if midpoints contains items --> Returns True if do
        if l[first_mid] == item or l[second_mid] == item:
            return True
        # Recursive call w/ list splice left of first_mid if item is less
        if item < l[first_mid]:
            return ternarySearchRec(l[:first_mid], item)
        # Recursive call w/ list splice right of second_mid if item is greater
        elif item > l[second_mid]:
            return ternarySearchRec(l[second_mid + 1:], item)
        # Recursive call w/ list slice in between first_mid & second_mid otherwise
        else:
            return ternarySearchRec(l[first_mid + 1:second_mid], item)

print(ternarySearchRec([1,2,3], 5))