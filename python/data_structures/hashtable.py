from data_structures.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=512):
        self.size = size
        self.buckets = [None] * self.size
        self.list_of_keys = []

    def hash(self, key):
        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)
        prime_sum = sum_of_chars * 257
        index_num = prime_sum % self.size
        return index_num

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self.buckets[index] = bucket
        bucket.insert((key, value))
        if key not in self.list_of_keys:
            self.list_of_keys.append(key)

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket == None:
            return None
        current = bucket.head
        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]
            current = current.next
        return None

    def contains(self,key):
        result = self.get(key)
        if result == None:
            return None
        else:
            return result

    def keys(self):
        return self.list_of_keys
