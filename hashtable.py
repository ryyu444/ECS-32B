# Code for a Hash Table

# Hash Function that returns a Hash Value
def hash_str(a_string, table_size):
    return sum([ord(c) for c in a_string]) % table_size

# Hash Table Class
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # Puts key-data pair into a position in the Hash Table
    def put(self, key, data):
        # Calls Hash_function to get a Hash Value to insert
        hash_value = self.hash_function(key, len(self.slots))

    # If slot at hash_value is None, inserts key-data pair respectively in Hash Table
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        # Else, there is already a key-data pair in Hash Value
        else:
            # If key is the same at the hash value, replace the data
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # Replace
            # Else, key is not the same, so call rehash function to find next slot
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                # While self.slots contains a key-data pair & self.slots does not equal key
                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot] != key
                ):
                # Continues to call rehash to get new next_slot
                    next_slot = self.rehash(next_slot, len(self.slots))

                # If key in next_slot is None, put key & data in Hash Table in next_slot
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                # Else, if nonempty slot already contains key, replace old data w/ new data
                else:
                    self.data[next_slot] = data

    # Hashes the key w/ modulo to produce a Hash Value
    def hash_function(self, key, size):
        return key % size

    # Rehashes values if old_hash has the same Hash Index as another key-data pair
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    # Gets data from a given key
    def get(self, key):
        # Gets the starting slot by calling hash_function w/ key
        start_slot = self.hash_function(key, len(self.slots))

        # Sets position to be starting slot
        position = start_slot
        # Iterates through Hash Table
        while self.slots[position] is not None:
            # If it finds a position that equals the key, it returns the data in that position
            if self.slots[position] == key:
                return self.data[position]
            # Else, it rehashes w/ the position and repeats the search
            else:
                position = self.rehash(position, len(self.slots))
                # If position becomes the start, there is no key corresponding to the data --> None
                if position == start_slot:
                    return None

    # Returns the data from the inputted key by calling get
    def __getitem__(self, key):
        return self.get(key)

    # Puts key-data pair into Hash Table by calling put
    def __setitem__(self, key, data):
        self.put(key, data)
