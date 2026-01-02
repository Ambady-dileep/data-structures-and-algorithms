# # FIRST APPROACH
# def count_occurrences(arr,target):
#     count=0 
#     for num in arr:
#         if num == target:
#             count+=1 
#     return count 
# arr = [10, 20, 10, 30, 20, 10, 40]

# print(count_occurrences(arr,10))

# # SECOND APPROACH
# def count_all(arr):
#     freq={}
#     for i in arr:
#         if i not in freq:
#             freq[i]=1 
#         else:
#             freq[i]+=1 
#     return freq
# arr = [10, 20, 10, 30, 20, 10, 40]

# print(count_all(arr))

# # THIRD APPROACH
# def count_all(arr):
#     freq = {}
#     for num in arr:
#         freq[num] = freq.get(num,0)+1 
#     return freq
# arr = [10, 20, 10, 30, 20, 10, 40]

# print(count_all(arr))