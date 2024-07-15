class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the 32-bit signed integer range.
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Edge case for overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result.
        negative = (dividend < 0) ^ (divisor < 0)

        # Convert both numbers to positive.
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize the quotient.
        quotient = 0

        # Subtract the divisor from the dividend until the dividend is smaller than the divisor.
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply the sign to the quotient.
        if negative:
            quotient = -quotient

        # Clamp the result within the 32-bit signed integer range.
        return max(MIN_INT, min(MAX_INT, quotient))

