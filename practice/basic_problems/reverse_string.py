# # FIRST APPROACH
# def reverse_str(s):
#     return s[::-1]

# print(reverse_str("Ambady"))
# print(reverse_str("Madam"))

# # SECOND APPROACH
# def reverse_str(s):
#     stack = list(s)
#     rev = ""
#     while stack:
#         rev += stack.pop()
#     return rev
# print(reverse_str("Ambady"))
# print(reverse_str("Madam"))

# # THIRD APPROACH
# def reverse_str(s):
#     rev = ""
#     for i in s:
#         rev = i + rev
#     return rev
# print(reverse_str("Ambady"))
# print(reverse_str("Madam"))

# # FOURTH APPROACH
# def reverse_str(s):
#     if len(s)<=1:
#         return s
#     return reverse_str(s[1:])+s[0]
# print(reverse_str("Ambady"))
# print(reverse_str("Madam"))