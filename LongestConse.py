# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         if not nums:
#             return 0

#         set_of_nums = set(nums)
#         uni = sorted(set_of_nums)
#         if len(uni) == 1:
#             return 1

#         common_differences = []
#         for i in range(1, min(4, len(uni))):
#             diff = uni[i] - uni[i - 1]
#             if diff not in common_differences:  # avoid duplicates
#                 common_differences.append(diff)

#         # Ensure difference 1 is included (for longest consecutive sequence)
#         if 1 not in common_differences:
#             common_differences.append(1)

#         max_len = 1

#         for d in common_differences:
#             for start in uni:
#                 if (start - d) in set_of_nums:
#                     continue

#                 length = 1
#                 curr = start

#                 while (curr + d) in set_of_nums:
#                     curr += d
#                     length += 1

#                 if length > max_len:
#                     max_len = length

#         return max_len

class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:
    if nums:
      nums_set = set(nums)
      max_len = 0           #Actual Output

      for i in nums_set:
        if (i-1) not in nums_set:
          curr = i
          length = 1

          while curr + 1 in nums_set:
            curr += 1
            length += 1

          max_len = max(length, max_len)

      return max_len
    return 0
