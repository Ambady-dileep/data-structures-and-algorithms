# <<--------------------Binary Search------------------------>>

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        print(f"Checking middle value: {arr[mid]} at index {mid}")

        if arr[mid] == target:
            print("Found target!")
            return mid
        elif arr[mid] < target:
            print(f"Going right (arr[mid] < target)")
            low = mid + 1
        else:
            print(f"Going left (arr[mid] > target)")
            high = mid -1
    print("Target not found.")
    return -1
    
arr = [1, 4, 7, 9, 12, 18, 25, 33, 45, 50]
target = 12

index = binary_search(arr, target)

print(f"\nResult: Target found at index {index}")