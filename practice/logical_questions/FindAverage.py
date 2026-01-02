# # FIRST APPROACH
# def sumofarr(arr):
#     total = 0
#     for i in arr:
#         total+=i 
#     avg = total/len(arr)
#     return avg
    
# arr = [2,4,1,3,5]
# print(sumofarr(arr))

# # SECOND APPROACH
# def sumofarr(arr):
#     return sum(arr)/len(arr)
    
# arr = [2,4,1,3,5]
# print(sumofarr(arr))

# # THIRD APPROACH
# def array_sum(arr, n):
#     if n == 0:
#         return 0
#     return arr[n-1] + array_sum(arr, n-1)

# arr = [10, 20, 30, 40, 50]
# average = array_sum(arr, len(arr)) / len(arr)
# print(average)
