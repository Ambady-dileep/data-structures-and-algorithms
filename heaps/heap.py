# 🔷 What is a Heap?
# A heap is a special kind of complete binary tree (all levels filled left to right) used to maintain priority.
# It must follow structural property and ordering property
# There are only two types of binary heaps:

# Type	      Root Node Holds	         Used For
# Min Heap	  Smallest value	   Priority queues, Dijkstra, Top-K largest
# Max Heap	  Largest value	       Leaderboards, Top-K smallest

# ⚠️ There is no "normal" heap — every heap is either a Min Heap or a Max Heap depending on the priority condition.

# 🔧 Difference Between Min Heap vs Max Heap

# 🔽 Min Heap:
# Parent ≤ Children
# Root is the minimum element
# ✅ Useful when you always want to extract the smallest item first

# Example (Min Heap):
#         2
#       /   \
#      5     10
#     / \   /
#    20  30 15

# 🔼 Max Heap:
# Parent ≥ Children
# Root is the maximum element
# ✅ Useful when you want to extract the largest item first

# Example (Max Heap):
#         50
#       /    \
#     30      40
#    /  \    /
#  10   20  35


class MaxHeap:
    def __init__(self):
        self.heap = [] 

    def insert(self,value):
        self.heap.append(value)
        self._bubble_up(len(self.heap)-1)

    def peek(self):
        return self.heap[0] if self.heap else None 
    
    def remove(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        self._swap(0,len(self.heap)-1)
        max_val = self.heap.pop()
        self._bubble_down(0)
        return max_val

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]: 
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < length and self.heap[left] > self.heap[largest]:  
                largest = left
            if right < length and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self._swap(index, largest)
            index = largest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
h = MaxHeap()
h.insert(20)
h.insert(5)
h.insert(50)     
h.insert(10)
print("Peek:", h.peek())      # 50
print("Remove:", h.remove())  # 50
print("Peek after:", h.peek())# 20


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add to end
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0] if self.heap else None

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap root with last, remove last, then heapify
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


h = MinHeap()
h.insert(10)
h.insert(5)
h.insert(30)
h.insert(2)

print("Peek:", h.peek())     # ➤ 2
print("Remove:", h.remove()) # ➤ 2
print("Peek after remove:", h.peek()) # ➤ 5



class MaxHeap:
    def __init__(self):
        self.heap = [] 
    
    def insert(self,value):
        self.heap.append(value)
        self._bubble_up(len(self.heap)-1)
        
    def peek(self):
        return self.heap[0] if self.heap else None 
    
    def _bubble_up(self,index):
        while index > 0:
            parent = (index-1)//2
            if self.heap[index] > self.heap[parent]:
                self._swap(index,parent)
                index = parent
            else:
                break

    def _bubble_down(self,index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index 
            
            if left < largest and self.heap[left] > self.heap[largest]:
                largest = left
            if right < largest and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break 
            self._swap(index,largest)
            index = largest 
            
    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop()
        self._swap(0,len(self.heap)-1)
        max_value = self.heap.pop()
        self._bubble_down(0)
        return max_value
        
    def show(self):
        print("Current Heap:", self.heap)

h = MaxHeap()
h.insert(20)
h.insert(5)
h.insert(50)
h.insert(10)
print("Peek:", h.peek())        # 50
print("Remove:", h.remove())    # 50
print("Peek after:", h.peek())  # 20
h.show()
