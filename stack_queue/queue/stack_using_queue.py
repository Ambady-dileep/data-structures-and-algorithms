# ------------------------------------------------------- #
# ------------------Stack using queue-------------------- #
# ------------------------------------------------------- #

class StackUsingQueue:
    def __init__(self):
        self.queue = []

    def push(self,x):
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
    
    def print(self):
        print(self.queue)

stack = StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print()
print(stack.pop())  
print(stack.peek()) 
stack.print() 
