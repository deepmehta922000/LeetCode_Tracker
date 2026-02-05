# Last updated: 2/5/2026, 10:20:05 AM
1from typing import List
2
3class Solution:
4    def makesquare(self, matchsticks: List[int]) -> bool:
5        total_sum = sum(matchsticks)
6        
7        # 1. Basic Check: Total length must be divisible by 4
8        if total_sum % 4 != 0:
9            return False
10        
11        # The length each side must reach
12        target_length = total_sum // 4
13        
14        # 2. Optimization: Sort matchsticks in descending order.
15        # This is CRITICAL. Trying the longest sticks first allows 
16        # the algorithm to fail early if a stick is too big,
17        # significantly pruning the search tree.
18        matchsticks.sort(reverse=True)
19        
20        # If the single longest stick is already longer than the target, return False
21        if matchsticks[0] > target_length:
22            return False
23
24        # Array to store the current length of each of the 4 sides
25        sides = [0] * 4
26
27        def backtrack(i):
28            # Base Case: All matchsticks have been placed
29            if i == len(matchsticks):
30                return True
31            
32            # Try placing the current matchstick in each of the 4 sides
33            for j in range(4):
34                # Only try to add the stick if it fits in this side
35                if sides[j] + matchsticks[i] <= target_length:
36
37                    sides[j] += matchsticks[i]
38                    if backtrack(i + 1):
39                        return True
40                    sides[j] -= matchsticks[i]
41                    
42            return False
43        return backtrack(0)