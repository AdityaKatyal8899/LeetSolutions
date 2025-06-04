class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        close_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return total

                if abs(total - target) < abs(close_sum - target):
                    close_sum = total
                
                elif total < target:
                    left += 1

                else:
                    right -= 1

        return close_sum
        