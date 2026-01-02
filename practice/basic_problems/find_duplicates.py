# # FIRST APPROACH - If the lengths differ, then duplicates existed.
# def containsDuplicate(nums):
#     return len(nums) != len(set(nums))

# nums = [1,2,4,2,3]
# print(containsDuplicate(nums))

# # SECOND APPROACH
# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
# nums = [1,6,4,2,3]
# print(containsDuplicate(nums))

# # THIRD APPROACH
# from collections import Counter
# def containsDuplicate(nums):
#     freq = Counter(nums)
#     for count in freq.values():
#         if count > 1:
#             return True
#     return False

# nums = [1,6,4,2,3]
# print(containsDuplicate(nums))

# # FOURTH APPROACH
# def containsDuplicate(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# nums = [1,6,4,2,3]
# print(containsDuplicate(nums))

# # FIFTH APPROACH
# def containsDuplicate(nums):
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             return True
#     return False

# nums = [1,6,4,2,3]
# print(containsDuplicate(nums))


# # Return all values that repeat (unique list of duplicates):
# def all_duplicates(nums):
#     seen = set()
#     dups = set()
#     for num in nums:
#         if num in seen:
#             dups.add(num)
#         else:
#             seen.add(num)
#     return list(dups)   # order unspecified
# # For [2,3,4,2,2] returns [2]
