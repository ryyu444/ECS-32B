# Ryan Yu
# ECS 32B A04
#
# Student ID: 919590656

# Problem 1 - Frisbee Sort

def frisbeeSort(frisbees):
    unsorted = True
    numsorted = len(frisbees) # Keeps track of sorted elements & position of last max value

    # Indefinite Loop that sorts until unsorted = False
    while unsorted:
        max = None
        
        # If frisbees is one or less, no need to sort
        if len(frisbees) <= 1:
            unsorted = False
            break

        # Step 1: Find biggest value - Loop through values in frisbee & compare to max value
        # If value is greater than max value, set max to be index of that value
        for i in range(numsorted):
            if max == None or frisbees[i] > frisbees[max]:
                max = i
        
        # Variables to store index of max & front of list for Step 2
        k = max
        h = 0

        # Step 2: Flips values at front w/ values up to max (Puts max at front)
        while h < k:
            temp = frisbees[k]
            frisbees[k] = frisbees[h]
            frisbees[h] = temp
            # Increments h to move right; Decrements k to move left
            h = h + 1
            k = k - 1

        # Variables to store index of front of list & area left to sort
        j = 0
        l = numsorted - 1

        # Step 3: Flips values at front w/ values up to but not including numsorted (Puts max in numsorted)
        while j < l:
            temp = frisbees[j]
            frisbees[j] = frisbees[l]
            frisbees[l] = temp
            # Increments j to move right; Decrements j to move left
            j = j + 1
            l = l - 1

        # Decrements numsorted by 1 after Steps 1, 2, 3 (To account for max being put in right place)
        numsorted = numsorted - 1

        # Once numsorted is 0, there is nothing left to sort --> unsorted = False
        if numsorted == 0:
            unsorted = False
    
    return frisbees # Returns sorted list

# l = [9,2,7,0,-1,5,10,18,32]
# print(frisbeeSort(l))

# Problem 2 - Bubble Sort from alternating ends

def bubbleSort(l):
    passes = 0 # Tracks num of passes (Used for alternating)

    # Sets num of elements to check per pass
    for i in range(len(l) - 1, 0, -1):
        
        # Bubble Sorts from left end of list for up to i-1 elements
        for j in range(i):
            # If passes is even, bubble sort by checking if current element > next element
            # Swaps them if they are, else moves onto next element
            if passes % 2 == 0:
                if l[j] > l[j+1]:
                    temp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = temp

        passes = passes + 1 # Increments passes by 1
        
        # Bubbles Sorts from right end of list for up to i-1 elements
        for h in range(i, 0, -1):
            # If passes is odd, bubble sort by checking if previous element > current element
            # Swaps them if they are, else moves onto next element
            if passes % 2 == 1:
                if l[h-1] > l[h]:
                    temp = l[h]
                    l[h] = l[h-1]
                    l[h-1] = temp

        passes = passes + 1 # Increments passes by 1

    return l # Returns sorted list

# h = [9, 3, 19, 4, 8, 13, 15, 6, 2, 16, 12, 5, 7, 17, 0, 1, 18, 14, 10, 11]
# print(bubbleSort(h))

# Problem 3 - Merge Sort w/o slicing

def mergeSort(l, start, stop):

# Ensures that sorting only occurs if more than one element is accessed
    if (start < stop): 

# Step 1: Break up list into smaller elements
        
    # Calculates middle index of list
        mid = (start + stop) // 2
        
    # Recursive Calls limit our scope of access to the indices of the list (Like breaking into smaller elements)
        mergeSort(l, start, mid) # Left "Sublist"
        mergeSort(l, mid + 1, stop) # Right "Sublist"
        
    # Variables to keep track of the index positions
        j = stop
        i = start
        h = mid
    
# Step 2: Sort the pairs

    # If start == stop, only one element can be accessed --> Return to escape
        if start == stop:
            return

    # Comparing left half & right half - Bubble Sort-like thing

    # While index for left half <= mid & index for right half >= mid, compare element in middle to left and right
    
        while i <= mid and j >= mid:

        # If l[h] > l[j] --> Swap middle w/ right element
        # Resets i & j to their original starting position to reiterate through the list
            if l[h] > l[j]:
                temp = l[h]
                l[h] = l[j]
                l[j] = temp
                i = start
                j = stop

        # If l[h] < l[i] --> Swap middle w/ left element
        # Resets i & j to their original starting position to reiterate through the list
            elif l[h] < l[i]:
                temp = l[h]
                l[h] = l[i]
                l[i] = temp
                i = start
                j = stop

        # Otherwise, neither elements match
        # Decrement right index by 1 (Starts at stop) & Increment left index by 1 (Starts at start)
            else:
                j = j - 1
                i = i + 1

    return l

# x = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
# print(mergeSort(x, 0, len(x) - 1))