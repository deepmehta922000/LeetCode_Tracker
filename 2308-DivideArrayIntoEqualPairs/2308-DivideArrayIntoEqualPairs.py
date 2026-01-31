# Last updated: 1/31/2026, 2:18:43 PM
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for count in counter.values():
            if count % 2 != 0:
                return False
        
        return True
        