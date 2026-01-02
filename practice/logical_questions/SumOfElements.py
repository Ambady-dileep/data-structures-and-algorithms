# FIRST APPROACH
def sumofarr(arr):
    result = 0
    for i in arr:
        result+=i
    return result
    
arr = [2,4,1,3,5]
print(sumofarr(arr))

# SECOND APPROACH
def sumofarr(arr):
    total = 0
    i = 0
    while i < len(arr):
        total+=arr[i]
        i+=1
    return total
    
arr = [2,4,1,3,5]
print(sumofarr(arr))

# THIRD APPROACH
arr = [4, 2, 7, 1]
print(sum(arr))   # 14

