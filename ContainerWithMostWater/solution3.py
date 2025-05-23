class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        for i in range(0, len(height) - 1):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)

        return max_area
        