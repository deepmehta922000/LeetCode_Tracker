# Last updated: 2/6/2026, 10:02:36 AM
1from typing import List
2
3class Solution:
4    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
5        total_sum = sum(nums)
6
7        # Basic check: total must be divisible by k
8        if (total_sum % k) != 0: 
9            return False 
10
11        target_sum = total_sum // k
12        
13        # Sort descending to improve backtracking pruning efficiency
14        nums.sort(reverse=True)
15        
16        # If the largest number exceeds the target, a valid partition is impossible
17        if nums[0] > target_sum:
18            return False
19            
20        # Tracks the current sum of each of the k subsets
21        subset_sums = [0] * k
22
23        def backtrack(current_num_idx):
24            if current_num_idx == len(nums):
25                return True
26            
27            current_val = nums[current_num_idx]
28
29            for subset_idx in range(k):
30                if subset_sums[subset_idx] + current_val <= target_sum:
31                    subset_sums[subset_idx] += current_val
32                    
33                    if backtrack(current_num_idx + 1):
34                        return True
35                    
36                    subset_sums[subset_idx] -= current_val
37                
38                # PRUNING: If the subset is empty (0) and the current number failed,
39                # it will fail in any other empty subset. Skip redundant branches.
40                if subset_sums[subset_idx] == 0:
41                    break
42                    
43            return False
44            
45        return backtrack(0)