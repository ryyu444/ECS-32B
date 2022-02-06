# Basic Templates for Sorting Algorithms

# Bubble Sorting - Checking adjacent values & adjusting 
def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1): # Defines range for j to search
        # Compares j element to next element & swaps if j is bigger than next
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# print(a_list)

# Short Bubble - Bubble Sort, but stops if no exchanges are made in a pass
def bubble_sort_short(a_list):
    for i in range(len(a_list) - 1, 0, -1): # Defines range for j to search
        exchanges = False
        # Compares to j element to next element --> Swaps if j is bigger than next
        # Turns exchanges = True, bc an exchange was made
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
        if not exchanges: # Breaks out of loop if no exchanges are made
            break

# a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
# bubble_sort_short(a_list)
# print(a_list)

# Selection Sort - Takes smallest/largest value from each pass & places in proper position after pass is done
def selection_sort(a_list): # Sorts by finding min value in this example
    for i, item in enumerate(a_list): # Gets index for items in list
        min_idx = len(a_list) - 1 # Gets last item index in list
        # Iterates through items & obtains min item index for each pass
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        # Once j loop is run & min index is not the first index, min value is swapped w/ first element in list
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# selection_sort(a_list)
# print(a_list)

# Insertion Sort - Sorts by maintaining a new sublist & inserting values from original
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i
        # Moves values greater than current val one position forward until current val is greater
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1] # Shifts previous val to current val pos
            cur_pos = cur_pos - 1 # Moves position to left one
        a_list[cur_pos] = cur_val # Inserts cur val when loop is done

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertion_sort(a_list)
# print(a_list)

# Shell Sort - Uses increments to make sublists that are i items apart --> Sorting w/ insertion
def shell_sort(a_list):
    sublist_count = len(a_list) // 2 # Creates 4 sublists
    while sublist_count > 0:
        for pos_start in range(sublist_count): # Sorts sublists
            gap_insertion_sort(a_list, pos_start, sublist_count)
        print("After increments of size", sublist_count, "the list is", a_list)
        sublist_count = sublist_count // 2 # Cuts sublist increment by half

# Sorts individual sublists created w/ a gap
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        # Moves bigger values to the right until the value is smaller than current
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap] # REPLACING VALUES instead of merging sublists
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val # Sets current position to have current value

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(a_list)
# print(a_list)

# Merge Sort - Recursively splitting lists until one item/empty list remains --> Sorting & Merging lists together
def merge_sort(a_list):
    print("Splitting", a_list)
    # Divides list in half recursively
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merges two smaller sorted lists into a larger sorted list 
        i, j, k = 0, 0, 0 # i = left half index; j = right half index; k = original list index

        # Merges values onto original list starting w/ smaller values & incrementing index counters
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]: # Ensures algorithm is stable by maintaining order of duplicate items in list
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        # Overrides values in original list with new sorted left half & increments index counters
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        # Overrides values in original list w/ new sorted right half & increments index counters
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging", a_list)

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# merge_sort(a_list)
# print(a_list)

# Quick Sort - Determines a pivot point --> Sorts list into left half being values less than pivot & right being bigger --> Halves are sorted
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

# Helper function that does recursive calls to sort original list
def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last) # Calls partition to create two sublists next to pivot
        quick_sort_helper(a_list, first, split - 1) # Recursive call to partition left sublist to organize
        quick_sort_helper(a_list, split + 1, last) # Recursive call to partition right sublist to organize

# Partitions the original list into two sublists w/ values left of pivot being less than pivot value & values right being greater
def partition(a_list, first, last):
    pivot_val = a_list[first] # Gets pivot value
    left_mark = first + 1 # Sets left mark to be index ahead of pivot
    right_mark = last # Sets right mark to be end of list
    done = False

    # Sorts list & puts values less than pivot to the left and values greater than pivot to the right of pivot by swapping marks
    while not done:
        # Moves left mark one position to the right if value at mark is less than pivot & left is less than right mark
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        # Moves right mark one position to the left if value at mark is greater than pivot & right is greater than left mark
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        # Once right mark is less than left mark, list is "sorted" by lower values on left & greater values on right
        if right_mark < left_mark:
            done = True
        # Swaps left mark w/ right mark & right mark w/ left mark IF left mark is greater than pivot & right mark is less than pivot
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first] # Swaps min value (contained in right mark) w/ pivot

    return right_mark # Returns index value for pivot value

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# quick_sort(a_list)
# print(a_list)