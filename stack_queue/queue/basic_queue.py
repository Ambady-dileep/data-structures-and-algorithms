# ✅ What is a Queue?
# A Queue is a linear data structure that follows the FIFO rule:
# First In, First Out

# 🔁 Meaning:
# The first element added to the queue is the first one to be removed.
# Think of a line at a movie theatre: the person who comes first gets served first.
# A Queue is like a line — whoever gets in first, gets out first.

# 🧠 Real-Life Analogy:

# Think of a bus queue:
# Front of the Line      Rear of the Line
#      [👴, 👨, 👧]  ← people in line
#       ↑          ↑
#    Dequeue      Enqueue
# 👴 entered first → leaves first (dequeue)
# 👧 came last → has to wait at the end (rear)


class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0 
    
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
        
    def display(self):
        return self.queue
        
    def peek_rear(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[-1]
        
    def peek_front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.is_empty())
q.dequeue()
print(q.display())
print(q.peek_rear())
print(q.peek_front())