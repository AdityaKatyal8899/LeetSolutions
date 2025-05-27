class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError("Cannot divide by zero.")
        
        # Handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine sign
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        temp_divisor = divisor
        num_shifts = 0

        # Find max shift without overflowing
        while (temp_divisor << 1) <= dividend:
            temp_divisor <<= 1
            num_shifts += 1

        # Subtract shifted divisors
        for i in range(num_shifts, -1, -1):
            if dividend >= (divisor << i):
                dividend -= (divisor << i)
                quotient |= (1 << i)

        return -quotient if negative else quotient
