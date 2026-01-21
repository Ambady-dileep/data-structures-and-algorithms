def bubble_sort(arr):
    n = len(arr)-1 
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [4, 2, 7, 1]
print(bubble_sort(arr))


# Practice code below - Just like a revision

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# arr = [4, 2, 7, 1]
# print(bubble_sort(arr))