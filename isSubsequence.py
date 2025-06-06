class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen = set()
        for i in t:
            if i not in seen:
                seen.add(i)

        for i in range(1, len(s)):
            if s[i-1] not in seen:
                return False
            

                
    

s  = Solution()

print(s.isSubsequence("axc", "ahbgc"))