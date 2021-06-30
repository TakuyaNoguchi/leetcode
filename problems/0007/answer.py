class Solution:
    def reverse(self, x: int) -> int:
        rev = int(''.join(reversed(list(str(abs(x))))))
        if rev < -2**31 or rev > (2**31 - 1):
            return 0

        return -rev if x < 0 else rev