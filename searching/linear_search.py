# <<--------------------Linear Search------------------------>>

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 25, 3, 7, 18, 42]
target = 7

print(linear_search(arr,target))
