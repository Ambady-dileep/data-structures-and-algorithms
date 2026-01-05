2️⃣ Space Complexity
Definition : Space Complexity measures how much memory your code uses relative to input size.

Includes memory for:

Variables
Data structures (arrays, dicts, etc.)
Function calls (recursion stack)

Examples
# O(1) space - constant
x = 10
y = 20
z = x + y

# O(n) space - linear
arr = [1,2,3,4,5]  # memory grows with n

# O(n^2) space - quadratic
matrix = [[0]*5 for _ in range(5)]  # n x n


Key point: Even if your code is fast (low time complexity) but uses too much memory, it will fail in real projects.