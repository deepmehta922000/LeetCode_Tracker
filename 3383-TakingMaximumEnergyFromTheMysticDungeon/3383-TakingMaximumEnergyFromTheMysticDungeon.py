# Last updated: 1/31/2026, 2:18:30 PM
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # n = len(energy)
        # ans = -inf

        # for i in range(n - k, n):
        #     total = 0
        #     j = i
        #     while j >= 0:
        #         total += energy[j]
        #         ans = max(ans, total)
        #         j -= k

        # return ans


        dp = energy[:]
        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)