class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        value = self.queue[self.front]
        if self.front == self.rear:
            # Only one element was present
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()      # Queue: 10 20 30 40
print("Dequeued:", cq.dequeue())  # 10
cq.enqueue(50)
cq.enqueue(60)    # Should show "Queue is full"
cq.display()      # Queue: 20 30 40 50
