# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         num = 0
#         length = 0
#         i=0
#         end = 0
#         if s is not None:
#             while i != len(s)-1:
#                 if len(s[end:i + 1]) == len(set(s[end:i + 1])):
#                     length = length + 1
#                     if length > num:
#                         num = length
#                 else:
#                     i = s.index(s[i], i - length, i)
#                     end = i+1
#                     length = 0
#                 i = i + 1
#         return num

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         dicts = {}
#         maxlength = start = 0
#         for i,value in enumerate(s):
#             if value in dicts:
#                 sums = dicts[value] + 1
#                 if sums > start:
#                     start = sums
#             num = i - start + 1
#             if num > maxlength:
#                 maxlength = num
#             dicts[value] = i
#         return maxlength

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         num = length = start = i = 0
#         dict = {}
#
#         while i < len(s):
#             if s[i] in dict:
#                 i = dict[s[i]] + 1
#                 if i > start:
#                     start = i
#                     length = 0
#                 else:
#                     length = length + 1
#             else:
#                 length = length + 1
#
#             if length > num:
#                 num = length
#
#             dict[s[i]] = i
#             i = i + 1
#         return num
# solution = Solution()
# length = solution.lengthOfLongestSubstring("afasfassssd")
# print(length)

