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
    

s = Solution()
print(s.isHappy(19))