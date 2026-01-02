# ⚡ What is O(1)?

# O(1) means "Constant Time Complexity."
# 👉 No matter how big your input is, the time taken by the code stays the same.
# O(1)	-->   Constant	-->  Accessing arr[i], dict[key]
# 📌 Simple Real-Life Example:

# Let’s say you walk into a room with 1000 people, and you just want to grab the first person’s name.
# You don't care about the rest.
# You don’t loop.
# You just go straight and ask.

# ➡️ That’s O(1) — one step, always.

# 🧠 Code Example in Python:
# arr = [10, 20, 30, 40]
# print(arr[0])  # Accessing first element → O(1)
# No matter if the list has 4 or 4 million elements — this line takes the same amount of time.

# 🔍 Common Examples of O(1):

# Operation	                             Reason it's O(1)

# Accessing a list element	          Index lookup is instant
# Getting dictionary value	          Hash lookup is constant time
# Checking if set has value	           Uses hashing underneath
# Swapping two variables	            One step, no loops
# Returning a fixed result	           No input dependency

# ⚠️ Why It Matters:
# O(1) is the fastest you can get.

# In interviews and real systems, aiming for O(1) solutions (when possible) shows you're efficient and smart.

