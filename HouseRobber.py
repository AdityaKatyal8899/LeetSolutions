from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        new_sum = 0
        for i in range(len(nums)):
            sum = nums[i] + self.largest(nums, i + 2)
            if sum > new_sum:
                new_sum = sum
        return new_sum

    def largest(self, nums, j):
        if j >= len(nums):
            return 0
        return max(nums[j] + self.largest(nums, j + 2), self.largest(nums, j + 1))

s = Solution()
l = [1, 2]
print(s.rob(l))  # Output: 2

l2 = [2, 7, 9, 3, 1]
print(s.rob(l2))  # Output: 12

l3 = [2, 1, 1, 2]
print(s.rob(l3))  # Output: 4