class Node(object):
    ''' Used to create a linked list for separate chaining in HashTable

    Attributes:
        key
        value
        next (Node): points to next node in linked list
    '''
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

class HashTable(object):
    def __init__(self, num_buckets=11):
        self.num_buckets = num_buckets
        self.size = 0
        self.__bucket_array = [None for _ in range(num_buckets)]

    def __str__(self):
        to_print = []
        for node in self.__bucket_array:
            while node is not None:
                to_print.append("%s: %s" % (node.key, node.value))
                node = node.next
        return "{%s}" % ", ".join(to_print)

    def is_empty(self):
        '''
        Returns boolean indicating whether a HashTable instance has no slots filled
        '''
        return self.size == 0

    def __get_bucket_index(self, key):
        '''
        Calculates index of key
        '''
        hash_code = hash(key)
        index = hash_code % self.num_buckets
        return index

    def load_factor(self):
        return self.size * 1.0 / self.num_buckets

    def get(self, key):
        '''
        Return value if key is present. Otherwise,
        return None
        '''
        bucket_index = self.__get_bucket_index(key)
        head = self.__bucket_array[bucket_index]

        # Look for key in chain
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        # Key not found
        return None

    def add(self, key, value):
        '''
        Add key and corresponding value to HashTable instance

        If load factor > 0.7, doubles the size of the bucket_array
        '''
        bucket_index = self.__get_bucket_index(key)
        head = self.__bucket_array[bucket_index]

        # Update value if key is already present
        while head is not None:
            if head.key == key:
                head.value = value
            head = head.next

        new_node = Node(key, value)

        # Check if there's a node at the index
        if head is None:
            self.__bucket_array[bucket_index] = new_node
        else:
            current_node = head
            new_node.next = current_node
            self.__bucket_array[bucket_index] = new_node

        self.size += 1

        # If load_factor > 0.7, double size of array
        if self.load_factor() > 0.7:
            new_num_buckets = 2 * self.num_buckets
            temp_bucket_array = self.__bucket_array
            new_bucket_array = [None for _ in range(new_num_buckets)]

            self.size = 0
            self.num_buckets = new_num_buckets
            self.__bucket_array = new_bucket_array

            for node in temp_bucket_array:
                while node is not None:
                    self.add(node.key, node.value)
                    node = node.next

    def remove(self, key):
        '''
        Remove key and corresponding value from HashTable instance
        '''
        bucket_index = self.__get_bucket_index(key)
        head = self.__bucket_array[bucket_index]

        previous = None

        while head is not None:
            if head.key == key:
                break
            else:
                previous = head
                head = head.next

        # Key not found
        if head is None:
            return None

        self.size -= 1
        if previous is not None:
            previous.next = head.next
        else:
            self.__bucket_array[bucket_index] = head.next

        return head.value


ht = HashTable()
print ht.size
ht.add("key", "value")
ht.add("hmmmm", "how bout this")
ht.add("123", "Test")
print ht.size
print ht.get("hmmmm")
print ht.remove("hmmm")
print ht
