from typing import List
class Solution: 
    def permute(self, nums: List[int], i = 0) -> List[List[int]]:
        res = []
        if i == len(nums):
            return [nums[:]]

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            res += self.permute(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
        return res
    def permuteUnique(self, nums: List[List[int]]) -> List[List[int]]:
        seen = set()
        curr = self.permute(nums)

        for i in curr:
              seen.add(tuple(i))
        return [list(i) for i in seen]
                
         

s =  Solution()

print(s.permuteUnique([1,1,2]))
