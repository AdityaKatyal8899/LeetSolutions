class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    if n == 1:
      return True
    
    if n%2 == 0:
      return self.isPowerOfTwo(n//2)
    return False
class Solution1:
  def isPow(self, n: int):
    return n > 0 and (n & (n-1)) == 0

s = Solution1()
print(s.isPow(16))

s1 = Solution()
print(s1.isPowerOfTwo(18))