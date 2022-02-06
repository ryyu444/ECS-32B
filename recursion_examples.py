# Some examples utilizing recursion

# Finds item in a list
def find(list, item):
    if list == []:
        return False
    if list[0] == item:
        return True
    else:
        return find(list[1:], item)

# Calculates up to n terms of Fibonacci Sequence
def fibonacci(term):
    if term <= 0:
        return 0
    if term == 1:
        return 1
    else:
        return fibonacci(term-1) + fibonacci(term-2)
    
print(fibonacci(5))

# Factorial calculator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

# List splicing
def splice(list, index):
    if list == []:
        return []
    elif index > len(list):
        return list
    elif index == 0:
        return []
    elif index > 0:
        return (splice(list, index-1) + [list[index-1]])

def spl(l, n):
 if l == [] or n <= 0:
  return []
 else:
  return [ l[0] ] + spl(l[1:], n-1) # Put first element & reduced total elements by 1

print(spl([1,2,3,4,5], 3))

print(splice([1,2,3,4,5], 5))

# Printing out contents of a list
def print_list(l):
 if l == []:
     return ""
 else:
     return str(l[0]) + " "  + print_list(l[1:])

print(print_list([1,2,3,4]))

# Print into recurse
# [1,2,3,4] -> [2,3,4] -> [3,4] -> [4] -> []
def print_list(l):
 if l == []:
    print('')
 else:
    print(l[0])
    print_list(l[1:])

print_list([1,2,3,4])

# Recurse into print
# [1,2,3,4] --> [1,2,3] --> [1,2] --> [1] --> [] --> Print
def print_list(l):
 if l == []:
  print('')
 else:
  print_list(l[:-1])
  print(l[-1])

print_list([1,2,3,4])

# Reverses a string
def reverse(string):
    if len(string) <= 1:
        return string
    else:
        return reverse(string[1:]) + string[0]

test = ""
print(reverse(test))

# Does a binary search on an ORDERED List with recursion
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

test = [1,2,3]
print(binarySearch(test,0))

# Searches for item in nodes recursively (Helper Function + Actual finder)
def NodeSearch(self, node, item):
    if node == None:
        return False
    else:
        if node.data == item:
            return True
        else:
            return self.NodeSearch(node.next, item)

def find(self,item):
    return self.NodeSearch(self.head, item)

# Searches for item in nodes recursively from END of list (Helper Function + Actual finder)
def NodeSearch2(self, node, item):
    if node == None:
        return False
    else:
        if node.data == item:
            return True
        else:
            return self.NodeSearch(node.prev, item)

def find2(self,item):
    return self.NodeSearch(self.tail, item)