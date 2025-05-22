class Solution:
    def maxArea(self, height: list[int]) -> int:
        heights = {i: h for i, h in enumerate(height)}
        maximum_area = 0

        for i in range(0, len(height) - 1):
            for j in range (i+1, len(height)):
                length = min(heights[i], heights[j])
                width = j - i
                area = length * width

                maximum_area = max(maximum_area, area)
        return maximum_area 
        