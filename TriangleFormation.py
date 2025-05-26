class Solution:
    def triangleType(self, nums: list[int]) -> str:
        i, j, k = nums

        if i + j <= k or k + j <= i or k + i <= j:
            return "none"
        if i == j == k:
            return "equilateral"
        if i == j or j == k or i == k: 
            return "isosceles"
        return "scalene"
    
    