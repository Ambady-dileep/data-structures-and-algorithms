class DoubleHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash1(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        return 1 + (hash(key) % (self.size - 1)) 

    def insert(self, key, value):
        index1 = self._hash1(key)
        index2 = self._hash2(key)

        for i in range(self.size):
            new_index = (index1 + i * index2) % self.size
            slot = self.table[new_index]

            if slot is None or slot[0] == key:
                self.table[new_index] = (key, value)
                return

        print("HashMap is full! Cannot insert:", key)

    def get(self, key):
        index1 = self._hash1(key)
        index2 = self._hash2(key)

        for i in range(self.size):
            new_index = (index1 + i * index2) % self.size
            slot = self.table[new_index]

            if slot is None:
                return None
            if slot[0] == key:
                return slot[1]
        return None

    def display(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")

d = DoubleHashMap(7)
d.insert("apple", 100)
d.insert("banana", 200)
d.insert("grape", 300)
d.insert("lemon", 400)
d.display()

print("Get grape:", d.get("grape"))
