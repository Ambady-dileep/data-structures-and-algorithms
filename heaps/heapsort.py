# 🔥 Why Is It Not Stable?
# Say you have:
# [('A', 5), ('B', 5)]
# Heap sort may swap their order because it only compares the key (5), not the order. So:

# ❌ ('A', 5), ('B', 5) → ('B', 5), ('A', 5)
# That’s why heap sort is NOT stable. 

def heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2 *i+2
    if left < n and arr[left]>arr[largest]:
        largest = left
    if right < n and arr[right]>arr[largest]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    
arr = [12,3,4,5,0,1]
heap_sort(arr)
print(arr)


def heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
        
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
        
arr = [12,3,4,5,0,1]
heap_sort(arr)
print(arr)


# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     if left < n and arr[left] > arr[largest]:
#         largest = left

#     if right < n and arr[right] > arr[largest]:
#         largest = right

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)

#     # Step 1: Build max heap
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     # Step 2: Extract elements from heap
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]  # swap max to end
#         heapify(arr, i, 0)  # heapify reduced heap

# arr = [12, 11, 13, 5, 6, 7]
# heap_sort(arr)
# print("Sorted array:", arr)
# # Output: [5, 6, 7, 11, 12, 13]




# def heapify(arr,n,i):
#     largest = i 
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if left < n and arr[left] > arr[largest]:
#         largest = left 
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]
#         heapify(arr,n,largest)
    
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2-1,-1,-1):
#         heapify(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[0],arr[i] = arr[i],arr[0]
#         heapify(arr,i,0)
        
# arr = [12, 11, 13, 5, 6, 7]
# heap_sort(arr)
# print("Sorted array:", arr)
    
    
# def heapify(arr,n,i):
#     largest = i
#     left = 2 * i + 1 
#     right = 2 * i + 2
#     if left < n and arr[left]>arr[largest]:
#         largest = left
#     if right < n and arr[right]>arr[largest]:
#         largest = right
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]
#         heapify(arr,n,largest)
        
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2-1,-1,-1):
#         heapify(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[0],arr[i] = arr[i],arr[0]
#         heapify(arr,i,0)
        
# arr = [12, 11, 13, 5, 6, 7]
# heap_sort(arr)
# print("Sorted array:", arr)
    
    
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

def heapify(arr,n,i):
    largest = i 
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
        
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)


    
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

def heapify(arr,n,i):
    largest = i 
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
        
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)