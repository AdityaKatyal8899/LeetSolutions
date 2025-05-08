class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        new = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in new:
                return [new[diff], i]
            new[num] = i
        return 