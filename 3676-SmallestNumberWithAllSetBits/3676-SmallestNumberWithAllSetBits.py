# Last updated: 1/31/2026, 2:18:25 PM
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x

        