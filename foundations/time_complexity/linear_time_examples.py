# 🚀 What is O(n)?
# O(n) means "Linear Time Complexity."
# 👉 The time increases in direct proportion to input size.
# O(n)  -->  Linear	-->  Loop over array

# So if:
# Input size is 10 → Code runs in 10 steps
# Input size is 1,000,000 → Code runs in 1,000,000 steps

# 📌 Real-Life Example:
# You're checking a bag full of chocolates to find the one with a golden wrapper (like Willy Wonka 🎫).
# You start from the top and check one by one.

# ➡️ That’s O(n) – you might have to check every single item.

# 🧠 Python Code Example:
# arr = [10, 20, 30, 40]

# # Print all elements → O(n)
# for x in arr:
#     print(x)
# If the list has 4 items → 4 steps
# If the list has 1000 items → 1000 steps


# 🔥 O(1) vs O(n): The Real Difference
# Feature	  O(1)	             O(n)
# Speed	   Always fast	   Slower as input grows
# Depends on size?	❌ No	✅ Yes
# Example	Accessing arr[0]	Looping through arr
# Visual	One punch ✅	     One punch per enemy in a crowd 🥊🥊🥊

# 📊 Example to Feel the Difference:
# # O(1)
# arr = [10, 20, 30, 40]
# print(arr[2])  # Always takes 1 step

# # O(n)
# for i in arr:
#     print(i)   # Takes as many steps as the size of arr

# 🧠 Motivation to Remember:

# O(1) is a sniper shot 🎯. O(n) is spraying bullets with an AK-47 😅. Both have their place — but if you can snipe, you win early.