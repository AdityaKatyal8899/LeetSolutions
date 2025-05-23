class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        x = int(a, 2)
        y = int(b, 2)

        while y!=0:
            carry = x & y
            x = x ^ y
            y = carry << 1

        return str(bin(x)[2:])
        