# # FIRST APPROACH
# def find_index(arr,target):
#     for i in range(len(arr)):
#         if target == arr[i]:
#             return i
#     return -1

# arr = [10, 20, 4, 45, 99]
# print(find_index(arr,4))

# # SECOND APPROACH
# def find_index(arr,target):
#     for i,j in enumerate(arr):
#         if j == target:
#             return i
#     return -1
        

# arr = [10, 20, 4, 45, 99]
# print(find_index(arr,4))

# # THIRD APPROACH
# arr = [10,20,30,40,50]
# print(arr.index(50))   # ➜ 4
