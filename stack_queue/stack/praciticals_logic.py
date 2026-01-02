# push() → insert at top
# pop() → remove from top
# peek() → see top without removing
# is_empty() → check if empty
# size() → count elements

class Stack:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,value):
        self.items.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None 
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None 
    
    def __str__(self):
        return f"Top to bottom {self.items}"
    
    def __len__(self):
        return len(self.items)
    
s = Stack()
s.push(10)
s.push(20)
print(s)
s.pop()
print(s)
print(s.peek())
print(len(s))

def reverse_string(string):
    stack = Stack()
    for s in string:
        stack.push(s)
    reversed_output = ""
    while not stack.is_empty():
        reversed_output+=stack.pop()
    return reversed_output

print(reverse_string("boss"))

# Need to practice below

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()

print(is_balanced("({[]})"))  # True
print(is_balanced("([)]"))    # False






