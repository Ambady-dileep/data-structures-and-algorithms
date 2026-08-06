# ✅ What is Merge Sort?
# Merge Sort is a Divide and Conquer algorithm.
# It divides the array into smaller parts, sorts them, and then merges them back together.

# ⚔️ Time & Space Complexity

# Case	Time
# Best	O(n log n) ✅
# Average	O(n log n) ✅
# Worst	O(n log n) ✅

# ✅ TL;DR — Why Learn Merge Sort First?

# Stable sort (doesn’t change order of equal elements)
# Guaranteed O(n log n) time in worst case
# Excellent with linked lists
# Builds your recursion skill 💪

# 🧠 KEY IDEA:
# Merge Sort splits by index.
# Quick Sort splits by pivot value.
# 🧠 Merge Sort = "Split by half ➝ Merge"
# 🔥 Quick Sort = "Split by pivot ➝ No Merge"

# Merge Sort:
# “Break everything into halves, sort them, then combine like a puzzle.”

# Quick Sort:
# “Put everything in its correct zone around a pivot, and recursively sort each zone.”

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

arr = [5, 3, 8, 1, 2]
print(merge_sort(arr))


# Practice code below - Just like a revision

def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    i=j=0 
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

arr = [2,4,1,7,3]
print(merge_sort(arr))



def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    mid = len(arr)//2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
    
def merge(left,right):
    result = []
    i=j=0
    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1 
        else:
            result.append(right[j])
            j+=1 
    result+=left[i:]
    result+=right[j:]
    return result
    
arr = [2,4,1,7,3]
print(merge_sort(arr))


def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    mid = (len(arr)//2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    i=j=0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
    
arr = [2,4,1,7,3]
print(merge_sort(arr))