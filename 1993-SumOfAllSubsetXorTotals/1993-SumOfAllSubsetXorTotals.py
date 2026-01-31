# Last updated: 1/31/2026, 2:18:52 PM
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        for num in nums:
             res = res | num
        
        return res * ( 2 ** (len(nums)-1) )


        
        def dfs(i, total):

            if i == len(nums):
                return total
            
            return dfs( i + 1, total ^ nums[i]) + dfs(i + 1, total)
    
        return dfs(0,0)