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
    for i in range(1,n):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [2,4,6,1,3]
print(insertion_sort(arr))

# Practice code below - Just like a revision

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         j=i-1
#         key = arr[i]
#         while j>=0 and arr[j] > key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr

# arr = [2,4,6,1,3]
# print(insertion_sort(arr))

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         j = i-1
#         key = arr[i]
#         while j>=0 and arr[j]>key:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#     return arr

# arr = [2,4,6,1,3]
# print(insertion_sort(arr))
