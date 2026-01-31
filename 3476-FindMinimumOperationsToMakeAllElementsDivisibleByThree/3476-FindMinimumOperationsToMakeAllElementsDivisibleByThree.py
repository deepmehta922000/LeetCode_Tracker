# Last updated: 1/31/2026, 2:18:29 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minOps = 0
        for num in nums:
            if num % 3 != 0:
                minOps += 1
        
        return minOps

        