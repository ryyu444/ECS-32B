# Base format for a deque

class Deque:

    def __init__(self):
        self.deque = []

    def add_front(self,item):
        self.deque.append(item)

    def add_rear(self,item):
        self.deque.insert(0,item)

    def remove_front(self):
        return self.deque.pop()

    def remove_rear(self):
        return self.deque.pop(0)

    def is_empty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)