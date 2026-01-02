# # FIRST APPOACH
# def find_min_max(arr):
#     if not arr or len(arr) < 2:
#         return f"Sorry please check the input"
#     min_val = max_val = arr[0]
#     for num in arr[1:]:
#         if num < min_val:
#             min_val = num 
#         elif num > max_val:
#             max_val = num 
#     return min_val,max_val
# arr = [10, 20, 5, 40, 15, -9, 60]

# print(find_min_max(arr))

# # SECOND APPROACH
# def find_min_max_sort(arr):
#     arr_sorted = sorted(arr)  # O(n log n)
#     return arr_sorted[0], arr_sorted[-1]
# arr = [10, 20, 5, 40, 15, -9, 60]

# print(find_min_max_sort(arr))

# # THIRD APPROACH
# arr = [10, 20, 5, 40, 15, -9, 60]
# print(min(arr), max(arr))
