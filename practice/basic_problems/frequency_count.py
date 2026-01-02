# # FIRST APPROACH
# def char_frequency(s):
#     freq = {}
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
#     return freq

# print(char_frequency("hello"))  
# # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# # SECOND APPROACH
# from collections import Counter
# s = "hello"
# print(Counter(s))