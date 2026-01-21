# 🧠 KEY IDEA:
# Merge Sort splits by index.
# Quick Sort splits by pivot value.
# 🧠 Merge Sort = "Split by half ➝ Merge"
# 🔥 Quick Sort = "Split by pivot ➝ No Merge"

# Merge Sort:
# “Break everything into halves, sort them, then combine like a puzzle.”

# Quick Sort:
# “Put everything in its correct zone around a pivot, and recursively sort each zone.”

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [8, 4, 7, 3, 9]
print(quick_sort(arr))  # Output: [3, 4, 7, 8, 9]


def quick_sort(arr):
    if len(arr)<=1:
        return arr 
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x<=pivot]
    right = [x for x in arr[:-1] if x>=pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

arr = [8, 4, 7, 3, 9]
print(quick_sort(arr))  # Output: [3, 4, 7, 8, 9]
