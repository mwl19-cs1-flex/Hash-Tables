class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
    
    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        # hash = 5381

        # for i in key:
        #     hash = ((hash << 5) + hash) + ord(i)

        # return hash & 0xFFFFFFFF

        hash = 5381
        str_byte = key.encode('utf-8')

        for i in str_byte:
            hash = ((hash*33)^i) % 0x100000000

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        cur_index = self.storage[index]
        if cur_index is not None:
            last_index = None
            while cur_index:
                if cur_index.key == key:
                    cur_index.value = value
                    return
                last_index = cur_index
                cur_index = cur_index.next
            last_index.next = HashTableEntry(key, value)
        else:
            self.storage[index] = HashTableEntry(key, value) 

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur_index = self.storage[index]
        if cur_index is not None:
            last_index = None
            while cur_index:
                if cur_index.key == key:
                    if last_index:
                        last_index.next = cur_index.next
                    else:
                        self.storage[index] = cur_index.next
            last_index = cur_index
            cur_index = cur_index.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur_index = self.storage[index]
        if cur_index is not None:
            while cur_index:
                if cur_index.key == key:
                    return cur_index.value
                cur_index = cur_index.next
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity = self.capacity * 2
        for i in self.storage:
            new_index = self.hash_index(self.storage[i].key)
            return new_index

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
