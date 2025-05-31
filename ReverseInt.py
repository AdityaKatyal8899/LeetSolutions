class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)  # Work with positive number only
        rev = 0

        while x != 0:
            digi = x % 10
            rev = rev * 10 + digi
            x = x // 10

        rev *= sign
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0      