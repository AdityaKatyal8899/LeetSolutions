from typing import List
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n%2 == 0:
            return float((nums[(n)//2] + nums[(n)//2 -1]) / 2)
            
        return float(nums[n//2])

nums1 = [1,3]
nums2 = [2]

print(findMedianSortedArrays(nums1, nums2))