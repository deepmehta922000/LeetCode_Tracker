# Last updated: 1/31/2026, 2:18:45 PM
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 122_444_5):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i