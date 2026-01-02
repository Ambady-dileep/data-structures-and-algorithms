# 🧠 What is Insertion Sort?
# Insertion Sort builds the final sorted array one element at a time,
# just like sorting a hand of playing cards 🃏.
# You pick one element, shift everything greater than it to the right, and insert it into its correct position.

# 📊 Visualization:

# Unsorted:
# [4, 3, 5, 1]
# First: take 3, insert before 4 → [3, 4, 5, 1]
# Next: 5 is already in place
# Then: insert 1 before all → [1, 3, 4, 5]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        print(f"Key is {key} at index {i}")
        j = i - 1
        while j >= 0 and arr[j] > key:
            print(f"{arr[j]} > {key} -> shifting {arr[j]} to position {j + 1}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Inserted key at position {j + 1} -> {arr}")
    return arr

arr = [5, 3, 2, 1]
print("Final Sorted Array:", insertion_sort(arr))


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key  
    return arr

arr = [5, 2, 4, 6, 1, 3]
print(insertion_sort(arr))
# ➜ [1, 2, 3, 4, 5, 6]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j=i-1
        key = arr[i]
        while j>=0 and arr[j] > key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
    
arr = [2,4,6,1,3]
print(insertion_sort(arr))











