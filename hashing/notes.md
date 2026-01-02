{
# Hash map v/s Hash set 
# | Feature        | HashMap              | HashSet                    |
# | -------------- | -------------------- | -------------------------- |
# | **Stores**     | Key → Value pairs    | Only values (no keys)      |
# | **Duplicates** | Keys must be unique  | Values must be unique      |
# | **Use Case**   | Lookup by key        | Check existence of a value |
# | **Example**    | `{“name”: “Ambady”}` | `{“apple”, “banana”}`      |

# Use a HashMap when:
# You need to associate one value with another (e.g., username → password, product → price).

# Use a HashSet when:
# You just care about unique elements and fast lookups (e.g., seen items, blocked users, duplicates remover).
}

{
# What is Rehashing?

# 🔴 If too many items get crammed into too few buckets → collisions increase, and performance drops.
# ✅ To fix this, rehashing is done:
# Increase the number of buckets (usually double).
# Recalculate (rehash) each key using the new size.
# Re-insert them into the new table.


# 📊 Example
# Say you have a small hash table of size = 4, and you keep inserting items.

# After a threshold (say 75% full = 3 items), rehashing triggers:

# # Imagine this internal process
# table = [None] * 4  # Original size

# # Adding keys:
# "apple" → index 0  
# "banana" → index 1  
# "mango" → index 1 (collision!)

# Rehashing triggered:
# ➡ Double table size → size = 8
# ➡ Recalculate index for each key using new size
# ➡ Insert each key into new table with updated index

# ⚠️ Important: Load Factor

# 💡 What is Load Factor?
# It tells you how full your hash table is.
# Load Factor = number of items / table size

# ⚠️ Why Load Factor Matters?

# Because as the load factor increases:
# Collisions increase ⚔️
# Performance drops ❌
# Hash table can no longer guarantee O(1) search/insert/delete
# So to avoid this, we keep the load factor below a threshold (usually 0.75 or 75%)
# If the load factor crosses a threshold (e.g., 0.75), rehashing occurs.
# This ensures O(1) lookup time on average is maintained.

# 🔁 What Happens When Load Factor Exceeds Threshold?
# → Rehashing is triggered:
# Create a new table with more buckets (usually double)
# Recompute the hash for each key
# Move all keys to new table (this is costly but rare)

# 🔥 Real Talk
# In Python, rehashing is automatic in dict and set. You don’t need to do it manually.
# But for interviews, custom hash tables, and performance tuning → you NEED to understand this.
}

{
# | Sorting Algorithm  | Time (Avg) | Space    | Stable?   | Use Cases                                |
# | ------------------ | ---------- | -------- | -------   | ---------------------------------------- |
# | **Bubble Sort**    | O(n²)      | O(1)     | ✅ Yes   | Teaching beginners, small datasets       |
# | **Insertion Sort** | O(n²)      | O(1)     | ✅ Yes   | Small arrays, nearly sorted data         |
# | **Selection Sort** | O(n²)      | O(1)     | ❌ No    | When memory writes are costly            |
# | **Merge Sort**     | O(n log n) | O(n)     | ✅ Yes   | Large stable sorts, linked lists         |
# | **Quick Sort**     | O(n log n) | O(log n) | ❌ No    | Fastest general-purpose sort for arrays  |
# | **Heap Sort**      | O(n log n) | O(1)     | ❌ No    | Constant space sorting, priority queues  |
# | **TimSort**        | O(n log n) | O(n)     | ✅ Yes   | Real-world hybrid sort (used in Python)  |
# | **Radix Sort**     | O(nk)      | O(n+k)   | ✅ Yes   | Sorting integers, strings in linear time |
}


{
# Double Hashing (A Type of Collision Resolution)

# Double Hashing is a technique to resolve collisions in open addressing
# Double Hashing - A collision-resolution method using a 2nd hash function
# Python dict/set handles rehashing and resizing internally, but doesn’t use double hashing
# No, double hashing is NOT the automatic resizing (doubling) of the table. It’s a technique used to handle collisions using a second hash function.
# So, Second Hash Function is used only:
# 🔄 When collision happens.
# During insertion or search (and deletion, if implemented).
# To compute step size and probe for the next available slot.
# If no collision → no second hash needed.
}

{
# Always mention “Python uses TimSort which is stable” when asked about sorting — it's a pro-level insight that impresses interviewers.
# | Algorithm                    | Stable?           |
# | ---------------------------- | ----------------- |
# | **Bubble Sort**              | ✅ Yes             |
# | **Insertion Sort**           | ✅ Yes             |
# | **Merge Sort**               | ✅ Yes             |
# | **TimSort** (used by Python) | ✅ Yes             |
# | **Quick Sort**               | ❌ No (by default) |
# | **Heap Sort**                | ❌ No              |
# | **Selection Sort**           | ❌ No              |
}

{
# what is Stable sorting?
# What is Timsort?

# | What         | Timsort                                                           |
# | ------------ | ----------------------------------------------------------------- |
# | Combines     | Merge Sort + Insertion Sort                                       |
# | Python Uses  | Yes, for `.sort()` and `sorted()`                                 |
# | Fastest For  | Real-world data, partially sorted, small inputs                   |
# | Stable?      | ✅ Yes (preserves equal-element order)                             |
# | Use It When? | Always — it's default in Python, no need to manually implement it |

# ⚙️ How Timsort Works — Step-by-Step

# 🔹 Step 1: Divide the data into runs

# A run is a small chunk of data that is already sorted (ascending or descending).
# If not sorted, it’s sorted using insertion sort.
# Usually run size = 32 or 64 elements (platform-dependent)

# 🔹 Step 2: Sort small runs using Insertion Sort

# Why? Because insertion sort is super fast for small arrays.
# Python sorts these small chunks first.

# 🔹 Step 3: Merge runs using Merge Sort

# Sorted runs are then merged together.
# Merging is done stably, preserving order of equal items.
# But TimSort doesn’t just blindly merge everything — it uses clever rules to merge efficiently (called "galloping mode").
}

{
# 🔐 Core Idea Behind Hash Table:

# You take a key (like "Ambady").
# Run it through a hash function → gives a number (called index).
# Use that number to store the value in an array (bucket).

# So it’s like:
# hash("Ambady") % size → index → go to that index → store/fetch value
}

{
# What are the operations that can be done in Stack and Queue?

# 🔹 Stack:
# push, pop, peek, is_empty, size
# 🔹 Queue:
# enqueue, dequeue, front, is_empty, size
}

{
# Explain how hash functions work ?

# A hash function is a function that takes a key (like a string, number, etc.)
# and converts it into an integer index in a fixed range (e.g., 0 to table size - 1).

# index = hash_function(key) % table_size
# That index decides where the value goes in the underlying array (called a bucket).
# Built-in Python hash() Function is there, 
# print(hash("Ambady"))  # → Some large integer
}

{
# What Is a Collision in Hashing?
# A collision occurs when two different keys produce the same hash index in a hash table.
# "abc" → 97+98+99 = 294 → 294 % 10 = 4
# "cab" → 99+97+98 = 294 → 294 % 10 = 4
# 🔥 Collision! Both keys map to index 4

# 🚧 Why Collisions Are Bad

# If collisions aren’t handled:
# New value overwrites existing value Or it gets lost completely Or the program crashes
# ❌ That breaks the hash table’s guarantee of O(1) lookups
}


{
# 🛡 How Do We Handle Collisions?

# ✅ 1. Chaining (Separate Chaining)
# Each bucket holds a list of key-value pairs
# If two keys hash to the same index, store both in a list at that index
# table[4] = [("abc", val1), ("cab", val2)]
# ✅ 2. Open Addressing : If a slot is full, find the next empty one

# ✅ TL;DR
# | Term      | Meaning                                               |
# | --------- | ----------------------------------------------------- |
# | Collision | Two different keys → same index in a hash table       |
# | Causes    | Limited buckets, many keys, imperfect hash functions  |
# | Fix It By | Chaining or Open Addressing (probing, double hashing) |
}

{
# Queue Operations: enqueue(), dequeue(), peek(), is_empty(), size(), display()
# Types of Queues: Simple Queue, Circular Queue, Deque, Priority Queue, Double-Ended Priority Queue
}

{
# 💥 What is a Monotonic Stack?
# A Monotonic Stack is a stack that keeps its elements in either increasing or decreasing order.

# 📘 Two Types:
# Type	Maintains
# Monotonic Increasing Stack	Smallest at bottom, largest at top
# Monotonic Decreasing Stack	Largest at bottom, smallest at top

# 💥 What is a Monotonic Queue?
# A Monotonic Queue is a double-ended queue (deque) where elements are kept in sorted order (non-increasing or non-decreasing).

# | Concept             | Used For                     | Structure    | Real Use              |
# | ------------------- | ---------------------------- | ------------ | --------------------- |
# | **Monotonic Stack** | Next Greater/Smaller Element | Stack (LIFO) | Histogram, stock span |
# | **Monotonic Queue** | Max/Min in Sliding Window    | Deque (FIFO) | Sliding window max    |
}

{
# 🧠 peek vs pop – What’s the Core Difference?
# Operation	What it Does	Removes the Element?	Time Complexity
# peek()	Returns the element at the top/front	❌ No	✅ O(1)
# pop()	Returns and removes the element at the top/front
# ⚔️ Peek is non-destructive. Pop is destructive.
}

{
# 💡 What is Linear Probing?
# Linear Probing is a collision resolution technique in open addressing where,if a slot is full, we simply check the next one (linearly) until we find an empty spot.
}

{
# 💡 What is a Circular Queue?
# A Circular Queue is a linear data structure that connects the end of the queue back to the front, forming a circle.
# This allows efficient use of space and avoids shifting elements like in a regular array-based queue.
}



Questions to practice 

Sort a string using stack
Number of occurrence word in a string using hash table
valid anagram using hash map
valid parenthesis
implement merge sort
valid anagram using hashtable
two sum in O n time
3rd largest element from unsorted array
