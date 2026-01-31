# Last updated: 1/31/2026, 2:18:23 PM
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        increasing_stack = []
        operations = 0

        for num in nums:
            while increasing_stack and (num < increasing_stack[-1]) : 
                increasing_stack.pop()
            
            if num == 0:
                continue
            
            if not increasing_stack or ( num > increasing_stack[-1]):
                operations += 1
                increasing_stack.append(num)
        
        return operations



        # increasing_stack = []
        # operations = 0

        # for num in nums:

        #     while increasing_stack and num < increasing_stack[-1]:
        #         increasing_stack.pop()

        #     if num == 0:
        #         continue
            
        #     if not increasing_stack or num > increasing_stack[-1]:
        #         operations += 1
        #         increasing_stack.append(num)
            
        
        # return operations