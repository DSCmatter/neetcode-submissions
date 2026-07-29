class Solution:
    def reverse(self, x: int) -> int:
        org = x  # Save the original number
        x = abs(x)  # Remove the sign

        # Convert to string, reverse it, and convert back to an integer
        res = int(str(x)[::-1])

        # Restore the sign if the original number was negative
        if org < 0:
            res *= -1

        # Check for 32-bit signed integer overflow
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0

        return res