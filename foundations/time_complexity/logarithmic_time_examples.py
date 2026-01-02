# 🧠 What is O(log n)?
# O(log n) means that with every step, the problem size gets divided by 2 (or 3, or some base — usually 2).
# It’s the opposite of O(n), where you go one-by-one.
# Here, you cut the problem in half every time.

# 🔥 Real-Life Example:
# You’re searching for a name in a phone book with 1000 pages.
# Instead of reading page 1, 2, 3, … 1000 (O(n)),
# you do this:
# Open to page 500 → too far!
# Go to page 250 → closer!
# Page 125 → almost there!
# Each time, you eliminate half the book.
# That’s O(log n) efficiency.

# 🧮 How Many Steps Does O(log n) Take?
# Let’s say you're dividing n by 2 repeatedly until you hit 1.

# n = 16
# → 16 → 8 → 4 → 2 → 1
# → Total steps = 4
# → log₂(16) = 4
# n	         log₂(n)steps
# 8	              3
# 16	          4
# 32	          5

# ✅ Code Example: Binary Search (Classic O(log n))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# Each loop cuts the array in half → O(log n)

# 🔥 Where You See O(log n)

# Algorithm / Task	        Why it's O(log n)?
# Binary Search	        Divide array in half each step

# 📌 Key to Remember:
# "O(n)" = Linear → Step-by-step
# "O(log n)" = Smart → Cut-in-half strategy
# "O(1)" = God-level → Instant