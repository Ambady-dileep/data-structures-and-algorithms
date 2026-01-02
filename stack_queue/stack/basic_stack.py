class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
        
    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
        
    def show_output(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i],end="->")
        print(None)
        
def reverse(string):
    stack = Stack()

    for s in string:
        stack.push(s)
        
    rev = ""
    while not stack.is_empty():
        rev+=stack.pop()
    return rev
    
def is_palindrome(string):
    stack = Stack()
    
    for s in string:
        stack.push(s)
    
    reversed_s = ""
    
    while not stack.is_empty():
        reversed_s+=stack.pop()
    return string == reversed_s

ss = Stack()
ss.push(10)
ss.push(20)
ss.push(30)
ss.show_output()
ss.pop()
ss.show_output()
print(ss.peek())
print(reverse("Hello"))
print(is_palindrome("medem"))

# ------------------------------------------------------- #
# ------------------Queue using Stack-------------------- #
# ------------------------------------------------------- #
class QueueUsingStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = [] 
        
    def enqueue(self,x):
        self.stack_in.append(x)
        
    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            return "Queue is empty"
            
        return self.stack_out.pop()
        
    def is_empty(self):
        return not self.stack_in and not self.stack_out
        
    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
                
        if not self.stack_out:
            return "Queue is empty"
            
        return self.stack_out[-1]
                
        
q = QueueUsingStack()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10
print(q.peek())     # 20
print(q.dequeue())  # 20
print(q.dequeue())  # 30

















class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackLL:
    def __init__(self):
        self.top = None 
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def is_empty(self):
        return self.top is None
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        value = self.top.data
        self.top = self.top.next
        return value
        
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
    
    def print(self):
        temp = self.top
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print(None)
    

def reverse_str(s):
    stack = StackLL()
    for ch in s:
        stack.push(ch)
        
    reverse_string=""
    while not stack.is_empty():
        reverse_string+=stack.pop()
    return reverse_string


sll = StackLL();
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
sll.print()
print(sll.pop())
print(sll.peek())
sll.print()
print(reverse_str("hello"))
    