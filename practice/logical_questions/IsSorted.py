# # FIRST APPROACH
# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True

# print(is_sorted([1, 2, 3, 4, 5]))   # True
# print(is_sorted([1, 3, 2, 4, 5]))   # False

# # SECOND APPROACH
# def is_sorted(arr):
#     return arr == sorted(arr)
# print(is_sorted([1,2,3,4,5]))