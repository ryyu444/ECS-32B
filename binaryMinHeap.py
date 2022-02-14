# Code to create a Binary MIN Heap Class

class BinaryMinHeap:
    
    def __init__(self):
        self._heap = []

    # Helper function to insert
    def _perc_up(self, cur_idx):
        # Goes through & finds parent nodes
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            # Compares value in parent to new node; Swaps parent w/ new node if new node < parent
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx # Sets current index to parent index

    # Appends item to end of heap & calls on perc_up to move it in proper place
    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    # Helper Function to delete that moves a node down to its proper spot in a tree
    def _perc_down(self, cur_idx):
        # While left child is less than heap size
        while 2 * cur_idx + 1 < len(self._heap):
            # Gets index for min child from current node
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

    # Helper function to perc_down that gets min child index
    def _get_min_child(self, parent_idx):
        # Returns left child if there is no right child (When index is greater than size of heap - 1)
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        # Returns left child if the value in the left child is less than right child value
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        # Returns right child otherwise
        return 2 * parent_idx + 2

    # Deletes the min value (root) of a tree
    def delete(self):
        # Swaps root value w/ last value in tree
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        # Pops out old root value (which is now at end of tree)
        result = self._heap.pop()
        # Moves new root to its proper place
        self._perc_down(0)
        return result

    # Builds an entire Heap from a list of keys
    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:] # Sets self._heap to be the list of not_a_heap
        cur_idx = len(self._heap) // 2 - 1 # Gets index of middle most value in list
        # While current index is >= 0
        while cur_idx >= 0:
            # The value at the index is compared to children & moved down to correct pos
            self._perc_down(cur_idx)
            # Current index is decremented to move to previous node
            cur_idx = cur_idx - 1

    def get_min(self):
        return self._heap[0]

    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)

a_heap = BinaryMinHeap()
a_heap.heapify([9, 5, 6, 2, 3])

while not a_heap.is_empty():
    print(a_heap.delete())
