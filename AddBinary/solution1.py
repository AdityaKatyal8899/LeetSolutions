class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(self.convert(a) + self.convert(b)))[2:]

    def convert(self, s):
        d = 0
        i = len(s) - 1

        for j in range (0, len(s)):
            d += int(s[j]) * 2 ** i
            i -= 1
        return d