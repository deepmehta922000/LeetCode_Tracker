# Last updated: 2/4/2026, 8:06:56 AM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3
4        res = []
5        current_partition = []
6
7        def backtrack(start_index):
8            # 1. Base Case: Have we partitioned the whole string?
9            if start_index >= len(s):
10                res.append(current_partition.copy()) # Add a copy of the valid path
11                return
12
13            # 2. Loop to find the next valid piece
14            for i in range(start_index, len(s)):
15                substring = s[start_index : i + 1]
16                if substring == substring[::-1]:
17                    
18                    # 3. Choose, Explore, Un-choose
19                    current_partition.append(substring)
20                    backtrack(i + 1)
21                    current_partition.pop()
22
23        backtrack(0)
24        return res