def bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [4, 2, 7, 1]
print(bubble_sort(arr))

# so here are so many things to review

# To know the working check the below+++++++

def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        print(f"\nPass {i + 1}:")
        for j in range(n - i):
            print(f"  Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"  Swapping {arr[j]} and {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"  After swap: {arr}")
            else:
                print(f"  No swap needed")
        print(f"End of pass {i + 1}: {arr}")
    return arr

arr = [1, 3, 4, 5, 6]
print("\nFinal sorted array:", bubble_sort(arr))

def bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr 
    
arr =[7,3,5,6,9,1]
print(bubble_sort(arr))

# Practice
def bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j]> arr[j+1]:
                arr[j+1],arr[j]= arr[j],arr[j+1]
    return arr 
    
    
arr = [2,4,1,7,3]
print(bubble_sort(arr))
def bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j]> arr[j+1]:
                arr[j+1],arr[j]= arr[j],arr[j+1]
    return arr 
    
    
arr = [2,4,1,7,3]
print(bubble_sort(arr))