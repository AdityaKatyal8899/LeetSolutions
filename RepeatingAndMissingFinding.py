class Solution:
  def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:

    l1 = [i for j in grid for i in j]
    has = {}

    for i, nums in enumerate(l1):
      if nums in has:
        repeat = nums
      has[nums] = i

    real_sum = len(l1)*(len(l1)+1) // 2
    unreal_sum = sum(l1)

    return [repeat, (real_sum - (unreal_sum - repeat))]


# s = Solution()
# l = [[1, 2, 3], [4, 5, 6], [7, 9, 9]]
# print(s.findMissingAndRepeatedValues(l))