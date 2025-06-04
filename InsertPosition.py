class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)

        if nums[n - 1] < target:
            return n
        
        low = 0
        high = n
        

        while low < high: 
            mid = (low+high) // 2

            if target < nums[mid]:
                high = mid

            elif target > nums[mid]:
                low = mid + 1
            
            else:
                return mid
        return low
    

s = Solution()

print(s.searchInsert([1,3,5,6], 2))