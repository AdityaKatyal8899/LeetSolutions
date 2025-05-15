class Solution:
  def myPow(self, x: float, n: int) -> float:

    if n == 0 or x == 1:
      return 1
    
    if n < 0:
      return 1/self.myPow(x,-n)
    a = self.myPow(x, n//2)

    if (n%2 == 0):
      return a*a
    
    return a*x*a
  
solution = Solution()

print(solution.myPow(2, 2))