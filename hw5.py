# Ryan Yu
# ECS 32B A04
#
# Student ID: 919590656

# Heap Sort w/ Heapify

class BinaryMinHeap:
    
    def __init__(self):
        self._heap = [] # Creates a list for the heap

    # Determines if the heap is empty or not
    def is_empty(self):
        return not bool(self._heap)

    # Turns items from a given sequence into a heap
    def heapify(self, l):
        # Goes through each item in sequence, appends it to the heap, & reheaps it into the correct position
        for i in range(len(l)):
            self._heap.append(l[i])
            self.reheapUp(i)

    # Helper Function to heapify that moves smaller nodes up the tree/heap until correct position is reached
    def reheapUp(self, cur_idx):
        # Goes through all parent nodes & compares their children to them
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            # Compares value in parent to current; Swaps parent w/ current if current < parent
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx # Sets current index to parent index

    # Helper Function to heapsort that moves larger nodes down the tree/heap until correct position is reached
    def reheapDown(self, cur_idx, end_idx):
        # Goes through children of current & compares it to current until end_idx (Index before sorted items) is reached
        while 2 * cur_idx + 1 < end_idx:
            # Gets index for smallest child of current node
            min_child_idx = self._get_min_child(cur_idx)
            # Swaps current node w/ min child if it is greater
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            # Otherwise, return the current node index as the smallest child index
            else:
                return
            cur_idx = min_child_idx

    # Helper function to ReheapDown that gets min child index
    def _get_min_child(self, parent_idx):
        # Returns left child if there is no right child (When index is greater than size of heap - 1)
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        # Returns left child if the value in the left child is less than right child value
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        # Returns right child otherwise
        return 2 * parent_idx + 2

    # Sorts the data in the heap
    def heapsort(self):
        last_sorted_idx = len(self._heap) - 1 # Sets the last sorted item index initially
        # Swaps first item in heap w/ last item in heap until the last sorted item index = 0 (When it reaches the root)
        # Calls on reheapDown while passing in last_sorted_idx to restore Heap Property by pushing new root to proper place
        while last_sorted_idx > 0:
            self._heap[0], self._heap[last_sorted_idx] = self._heap[last_sorted_idx], self._heap[0]
            last_sorted_idx -= 1
            self.reheapDown(0, last_sorted_idx)

    # Returns the last value/node in the heap
    def last_val(self):
        # Pops out old root value (which is now at end of tree)
        result = self._heap.pop()
        # Moves new root to its proper place
        return result


# a_heap = BinaryMinHeap()
# a_heap.heapify([5, 2, 1, 4, 3])
# a_heap.heapsort()

# print(a_heap._heap)

# while not a_heap.is_empty():
#     print(a_heap.last_val())