class Solution:
    def stoi(self, s):
        res = 0
        n = False
        start = 0

        if s[0] == "-":
            n = True
            start = 1
        elif s[0] == "+":
            start = 1

        for i in range(start, len(s)):
            digi = ord(s[i]) - ord("0")
            if digi < 0 or digi > 9:
                return 0
            res = (res * 10) + digi

        if n:
            return -res
        return res

    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        while i < n and s[i] == " ":
            i += 1

        # Sign detection
        if i < n and (s[i] == "-" or s[i] == "+"):
            sign = s[i]
            i += 1
        else:
            sign = ""

        start = i

        # Read digits
        while i < n and '0' <= s[i] <= '9':
            i += 1

        res = sign + s[start:i]

        if not res or res in ["-", "+"]:
            return 0

        res1 = self.stoi(res)

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        res1 = max(INT_MIN, min(res1, INT_MAX))

        return res1
