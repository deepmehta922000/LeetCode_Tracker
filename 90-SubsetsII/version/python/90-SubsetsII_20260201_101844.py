# Last updated: 2/1/2026, 10:18:44 AM
1from typing import List
2
3class Solution:
4    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
5        res = []
6        current_subset = []
7        
8        # 1. Sort the input array to handle duplicates.
9        nums.sort()
10
11        def backtrack(start_index):
12            # Add the current subset as a valid solution.
13            res.append(current_subset.copy())
14
15            # Explore further options by adding more numbers.
16            for i in range(start_index, len(nums)):
17                # 2. Add the condition to skip duplicates.
18                # If the current element is the same as the previous one,
19                # and we are not at the start of the loop for this level, skip it.
20                if i > start_index and nums[i] == nums[i-1]:
21                    continue
22                
23                # Choose, Explore, Un-choose pattern
24                current_subset.append(nums[i])
25                backtrack(i + 1)
26                current_subset.pop()
27
28        backtrack(0)
29        return res