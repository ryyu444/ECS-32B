# List of Searches

# Sequential Search - Linearly going through list & checking the value
def ordered_sequential_search(a_list, item):
    pos = 0
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            if a_list[pos] > item:
                return False
            else:
                pos = pos + 1
    return False

# Binary Search (Nonrecursive + Recursive) - Uses middle value & searches by cutting list
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

def binarySearch(list,item):
    # If list has one element, checks to see if that element is the item
    if len(list) == 1: 
        return list[0] == item
    else:
        # Gets the middle index of the list
        index = (len(list)) // 2
        # If middle value in list is item, return true
        if list[index] == item:
            return True
        # Else, if the item is bigger than mid val --> Recurse w/ list slice of values above index
        elif item > list[index]:
            return binarySearch(list[index:],item)
        # Else if item is smaller than mid val --> Recurse w/ list slice of values below index
        else: 
            return binarySearch(list[:index],item)

# Binary Search where speeds are O(logn) - NO LIST SLICING
def binarySearch(list,start, stop, item):
    if list == []:
        return False
    # If list has one element, checks to see if that element is the item
    if start == stop: 
        return list[start] == item
    else:
        # Gets the middle index of the list
        mid = (start + stop) // 2
        # If middle value in list is item, return true
        if list[mid] == item:
            return True
        # Else, if the item is bigger than mid val --> Recurse w/ list slice of values above index
        elif item > list[mid]:
            return binarySearch(list, mid + 1, stop, item)
        # Else if item is smaller than mid val --> Recurse w/ list slice of values below index
        else: 
            return binarySearch(list, start, mid - 1, item)

def binaryResult(list, item):
    return binarySearch(list, 0, len(list)-1, item)