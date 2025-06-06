class Solution:
  def coloredcells(self, n: int) -> int:
    return 2*(n**2) - (2*n) + 1
  

s = Solution()
print(s.coloredcells(3))