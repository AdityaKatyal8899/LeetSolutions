class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_indices = [j for j in range(n) if nums[j] == key]
        res = []
        for i in range(n):
            for j in key_indices:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        
        return res
        