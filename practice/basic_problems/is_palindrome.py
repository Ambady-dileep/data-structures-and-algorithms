# # FIRST APPROACH
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False

# # SECOND APPROACH
# def is_palindrome(s):
#     left, right = 0, len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False

# # THIRD APPROACH - RECURSION
# def is_palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
# print(is_palindrome("racecar"))