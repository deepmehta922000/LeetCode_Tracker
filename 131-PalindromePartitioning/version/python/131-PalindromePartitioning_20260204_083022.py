# Last updated: 2/4/2026, 8:30:22 AM
1from typing import List
2
3class Solution:
4    def partition(self, s: str) -> List[List[str]]:
5        n = len(s)
6        res = []
7        part = []
8
9        # 1. Pre-compute palindromes using 2D DP
10        # dp[i][j] is True if s[i...j] is a palindrome
11        dp = [[False] * n for _ in range(n)]
12        
13        # We iterate through the string to fill the DP table.
14        # 'length' is the length of the substring we are checking.
15        for length in range(1, n + 1):
16            for i in range(n - length + 1):
17                j = i + length - 1
18                
19                # A substring s[i...j] is a palindrome if:
20                # 1. The characters at the ends match (s[i] == s[j])
21                # 2. AND (the length is <= 2 OR the inner substring is a palindrome)
22                if s[i] == s[j]:
23                    if length <= 2 or dp[i + 1][j - 1]:
24                        dp[i][j] = True
25
26        def dfs(start: int):
27            # Base Case: If we've reached the end of the string, 
28            # we've found a valid partition.
29            if start == n:
30                # In Python, we must append a copy of the list: part[:] or list(part)
31                res.append(list(part))
32                return
33
34            # Try every possible end index for the current substring
35            for i in range(start, n):
36                # 2. O(1) Check using our pre-computed DP table
37                if dp[start][i]:
38                    # Choose: Add the current palindrome substring to our path
39                    part.append(s[start : i + 1])
40                    
41                    # Explore: Move to the next start index
42                    dfs(i + 1)
43                    
44                    # Un-choose: Backtrack to try a different partition
45                    part.pop()
46
47        dfs(0)
48        return res
49
50
51# class Solution:
52#     def partition(self, s: str) -> List[List[str]]:
53
54#         res = []
55#         current_partition = []
56
57#         def backtrack(start_index):
58#             # 1. Base Case: Have we partitioned the whole string?
59#             if start_index >= len(s):
60#                 res.append(current_partition.copy()) # Add a copy of the valid path
61#                 return
62
63#             # 2. Loop to find the next valid piece
64#             for i in range(start_index, len(s)):
65#                 substring = s[start_index : i + 1]
66#                 if substring == substring[::-1]:
67                    
68#                     # 3. Choose, Explore, Un-choose
69#                     current_partition.append(substring)
70#                     backtrack(i + 1)
71#                     current_partition.pop()
72
73#         backtrack(0)
74#         return res