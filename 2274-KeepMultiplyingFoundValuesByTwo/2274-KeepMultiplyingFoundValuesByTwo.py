# Last updated: 1/31/2026, 2:18:44 PM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numsSet = set(nums)
        while original in numsSet:
            original *= 2

        return original
        