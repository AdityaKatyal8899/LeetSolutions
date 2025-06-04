class Solution:
    def isHappy(self, n: int) -> bool:
        if 0 <= n <= 9 and n != 1:
            return False
        if n == 1:
            return True

        suum = 0
        n1 = str(n)

        i = 0
        while i < len(n1):
            suum += int(n1[i]) ** 2
            i += 1
        if suum == 1:
            return True
        return False
    
class Solution1:
        
    def isHappyy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        
        return True   
        
                
            
        
    

s = Solution()
print(s.isHappy(19))