# 💥 What is O(n log n)?
# O(n log n) means: "You're doing a log n operation for each of the n items."
# Merge Sort	✅ O(n log n)	Fast, Stable

# ✅ Divide & Conquer (O(n log n)):

# Split into 2 halves
# Sort each half
# Merge the results
# 🔥 Result? 100,000 numbers sorted in seconds, not hours.

# It’s a combo of:
# n = you visit every item once
# log n = and for each, you do some kind of divide-and-conquer or binary-style step
# 🔥 log n part means:
# You’re cutting the data in half again and again — that’s the divide step.

# 🔥 n part means:
# You're doing that cutting work across all n elements.

# 💡 Real Meaning:
# Think of it as: "Loop over n things + do something smart like binary search/divide inside the loop."

# 🔍 Real-Life Example:
# Imagine sorting exam papers:
# You have to touch every paper at least once → O(n)
# But instead of comparing each with all others (O(n²)),
# you use smart merging/splitting → O(log n)
# ➡️ Total: O(n log n)

# ✅ Most Common Example: Merge Sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# You divide (log n levels of recursion)
# At each level, you merge n elements total
# ➡️ Total time: O(n log n)

# 🔎 Breakdown using Merge Sort as example:
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# 📊 What happens here?
# Let’s say n = 8
# ✅ Step 1: Divide (log n levels)
# First: [8 elements]
# Divide → [4] [4]
# Divide → [2][2][2][2]
# Divide → [1][1][1][1][1][1][1][1] → Done.

# So how many levels did we divide?
# 8 → 4 → 2 → 1  
# That’s 3 levels → log₂(8) = 3
# ✔️ That’s the log n part.


















