class Node(object):

    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        acc = []
        cursor = self
        while cursor is not None:
            acc.append(cursor.value)
            cursor = cursor.next
        return str(acc)

class HashTable(object):
    def __init__(self, num_buckets=11):
        self.num_buckets = num_buckets
        self.size = 0
        self.bucket_array = [None for _ in range(num_buckets)]

    def is_empty(self):
        '''
        Returns boolean indicating whether a HashTable instance has no slots filled
        '''
        return self.size == 0

    def get_bucket_index(self, key):
        '''
        Calculates index of key
        '''
        hash_code = hash(key)
        index = hash_code % self.num_buckets
        return index

    def load_factor(self):
        return self.size * 1.0 / self.num_buckets

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        # Look for key in chain
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        # Key not found
        return None

    def add(self, key, value):
        bucket_index = self.get_bucket_index(key)

        # TODO: check if key is already in array

        self.size += 1
        head = self.bucket_array[bucket_index]
        new_node = Node(key, value)

        # Check if chain at index
        if head is None:
            self.bucket_array[bucket_index] = new_node
        else:
            current_node = head
            new_node.next = current_node
            self.bucket_array[bucket_index] = new_node


        # If load_factor > 0.7, double size of array
        if self.load_factor() > 0.7:
            new_num_buckets = 2 * self.num_buckets
            temp_bucket_array = self.bucket_array
            new_bucket_array = [None for _ in range(new_num_buckets)]

            self.size = 0
            self.num_buckets = new_num_buckets
            self.bucket_array = new_bucket_array

            for node in temp_bucket_array:
                while node is not None:
                    self.add(node.key, node.value)
                    node = node.next



ht = HashTable()
print ht.size
print ht.get_bucket_index("hey")
ht.add("key", "value")
ht.add("hmmmm", "how bout this")
ht.add("123", "Test")
print ht.bucket_array