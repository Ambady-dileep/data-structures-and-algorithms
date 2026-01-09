def bubble_sort(arr):
    n = len(arr)-1 
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [4, 2, 7, 1]
print(bubble_sort(arr))
