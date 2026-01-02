# <<--------------------Linear Search------------------------>>

def linear_search(arr,target):
    for i in range(len(arr)):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == target:
            print("Target found")
            return i
        print("Target not Found!")
    return -1

arr = [10, 25, 3, 7, 18, 42]
target = 7

index = linear_search(arr,target)
print(f"\nResult: Target found at index {index}")


# arr = [1, 4, 7, 9, 12, 18, 25, 33, 45, 50]
# target = 12

# def binary_search(arr,target):
#     low = 0 
#     high = len(arr)-1
#     while low < high:
#         mid = (low+high)//2
        
#         if arr[mid]==target:
#             print("Found target")
#             return print(f"Mid value is {arr[mid]} and index is {mid}")
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
    
    
# print(binary_search(arr,target))


# arr = [5, 13, 8, 4, 9]
# target = 8

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return f"The index is {i} and value is {arr[i]}"
#     return -1

# print(linear_search(arr,target))

# def linear_search(arr, target):
#     for i, value in enumerate(arr):   # i = index, value = element
#         if value == target:
#             return i
#     return -1

# arr = [5, 13, 8, 4, 9]
# target = 8
# print(linear_search(arr,target))

# def binary_search(arr,target):
#     low = 0 
#     high = len(arr)-1
#     while low < high:
#         mid = (low+high)//2  
#         if arr[mid]== target:
#             return mid 
#         elif arr[mid]<target:
#             low = mid + 1
#         else:
#             high = mid - 1 
#     return -1 
    
# print(binary_search(arr,target))    
