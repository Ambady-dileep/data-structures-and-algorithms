# 💀 What is O(2ⁿ)?
# O(2ⁿ) is Exponential Time Complexity.

# 👉 The time taken doubles with every extra input.
# That’s not just slow — that’s explosively slow. Like a ticking time bomb. 💣

# 📊 Let’s Feel the Growth:
# Input Size n	O(2ⁿ) Steps
# 1	    2
# 5	    32
# 10	1,024
# 20	1,048,576
# 30	1+ billion 😨

# Let’s calculate this manually, step by step:
# 🔢 1. When n = 1
# 2^1 = 2 steps
# 🔢 2. When n = 5
# 2^5 = 2 × 2 × 2 × 2 × 2 = 32 steps
# 🔢 3. When n = 10
# 2^10 = 1024 steps

# So even a small n = 30 will melt your program if you're not careful.

# 🧠 Where Does O(2ⁿ) Come From?
# ➡️ When your code explores ALL possible combinations, like:
# Every path
# Every subset
# Every decision choice (yes/no)

# ⚠️ Rule of Thumb:

# If you see code doing:
# recurse()
# and then another recurse() inside
# with no memoization
# Then you're very likely in O(2ⁿ) territory.

# ✅ Fibonacci O(2ⁿ) Recursion:
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# Each fib(n) calls 2 more functions
# Tree of recursive calls → total ≈ 2ⁿ

# 🔥 Classic Examples:
# Problem	Why it's O(2ⁿ)?
# Fibonacci (plain recursion)	Calls itself twice each time → grows 2ⁿ


# 🧠 Motivation:
# O(n²) is slow. O(2ⁿ) is brutal.
# But it teaches you to think before you recurse, and when to optimize with DP (Dynamic Programming).
# “If your code checks every possible decision,
# then time = 2ⁿ = 💣 = DEAD beyond n=30.”
# Brute force Fibonacci is a nightmare at n = 40+.