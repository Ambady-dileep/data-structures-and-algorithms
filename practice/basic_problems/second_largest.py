# # FIRST APPROACH
# arr = [10, 20, 4, 45, 99]
# arr.sort()
# print(arr[-2])

# # SECOND APPROACH
# def second_lar(arr):
#     unique = list(set(arr))
#     result = unique[-2]
#     return result

# arr = [4,6,3,2,9]
# print(second_lar(arr))

#THIRD APPROACH
def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float("-inf")
    for num in arr:
        if num > first:
            second = first 
            first = num
        elif num != first and num > second:
            second = num
    return second if second != float("-inf") else None 

arr = [10, 20, 4, 45, 99]
print(second_largest(arr))
