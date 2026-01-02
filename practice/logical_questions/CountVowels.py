# # FIRST APPROACH
# def count_vowels(s):
#     count = 0
#     vowels = 'aeiouAEIOU'
#     for i in s:
#         if i in vowels:
#             count+=1
#     return count
# print(count_vowels("hello"))

# # SECOND APPROACH
# s = "Hello World"
# count = sum(1 for i in s if i.lower() in "aeiou")
# print(count)