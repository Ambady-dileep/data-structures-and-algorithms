# table_size = 10
# key = "apple"
# hash_value = hash(key)
# ans = hash_value % table_size
# print(ans)

# class HashMap:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def _hash(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self._hash(key)
#         bucket = self.table[index]

#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return
#         bucket.append((key, value))

#     def get(self, key):
#         index = self._hash(key)
#         bucket = self.table[index]

#         for k, v in bucket:
#             if k == key:
#                 return v
#         return None

#     def delete(self, key):
#         index = self._hash(key)
#         bucket = self.table[index]

#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 return True
#         return False


# h = HashMap()

# h.insert("apple", 10)
# h.insert("banana", 20)
# print(h.get("apple"))     # 10
# print(h.get("banana"))    # 20

# h.insert("apple", 99)
# print(h.get("apple"))     # 99 (updated)

# h.delete("banana")
# print(h.get("banana"))    # None


class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
        
    def insert(self,key,value):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]  

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


h = HashMap()

h.insert("apple", 10)
h.insert("banana", 20)
print(h.get("apple"))     # 10
print(h.get("banana"))    # 20

h.insert("apple", 99)
print(h.get("apple"))     # 99 (updated)

h.delete("banana")
print(h.get("banana"))    # None

##########################################################################################################

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0  # to track number of keys

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    # 🔹 For print(h)
    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.table):
            result += f"{i}: {bucket}\n"
        return result

    # 🔹 For len(h)
    def __len__(self):
        return self.count

    # 🔹 For "key" in h
    def __contains__(self, key):
        return self.get(key) is not None

    # 🔹 For h["Apple"]
    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(f"{key} not found")
        return value

    # 🔹 For h["Apple"] = 10
    def __setitem__(self, key, value):
        self.insert(key, value)


h = HashMap()
h["Apple"] = 10
h["Orange"] = 20
h["Mango"] = 30

print(h["Apple"])         # 10
print("Mango" in h)       # True
print(len(h))             # 3
del h["Orange"]
print(len(h))             # 2
print(h)                  # Prints all buckets

######################################################################################################################################

class HashMap:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))

    def get(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for k,v in bucket:
            if k == key:
                return v
        return None 

    def delete(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        result = ""
        for i,bucket in enumerate(self.table):
            result+=f"Index is {i}:{bucket}\n"
        return result 
        
h = HashMap(10)
h.insert("apple",10)
h.insert("banana",20)
h.insert("orange",30)
print(h.get("apple"))
print(h.delete("apple"))
        
        

class HashMap:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self,key):
        return hash(key)%self.size
        
    def insert(self,key,value):
        index = self._hash(key)
        bucket = self.table[index]
        for (i,(k,v)) in enumerate(bucket):
            if k == key:
                bucket[i]=(key,value)
                return 
        bucket.append((key,value))
        
    def get(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for k,v in enumerate(bucket):
            if k == key:
                return v
        return None
        
    def delete(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
            return False
            
    def __str__(self):
        result = ""
        for i,bucket in enumerate(self.table):
            result+=f"Index is {i}: {bucket}\n"
        return result
        

h = HashMap(10)
h.insert("apple",10)
h.insert("banana",20)
h.insert("orange",30)
print(h.get("apple"))
print(h.delete("apple"))
print(h)


class HashMap:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]
        
    def _hash(self,key):
        return hash(key) % self.size
        
    def insert(self,key,value):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return 
        bucket.append((key,value))
            
    def get(self,key):
        index =  self._hash(key)
        bucket = self.table[index]
        
        for k,v in bucket:
            if k == key:
                return v
        return None
                
    def delete(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for i,(k,v) in enumerate(bucket):
            if k == key:
                print(bucket[i])
                del bucket[i]
                return True
        return False
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index{i}:{bucket}")


h = HashMap(4)
h.insert("Apple",10)
h.insert("Orange",20)
print(h.get("Apple"))
h.display()
