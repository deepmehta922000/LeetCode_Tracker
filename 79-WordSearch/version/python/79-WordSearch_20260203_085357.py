# Last updated: 2/3/2026, 8:53:57 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        ROWS, COLS = len(board), len(board[0])
4        path = set()
5
6        def dfs(r, c, i):
7            if i == len(word):
8                return True
9            
10            if (min(r, c) < 0 or
11                r >= ROWS or c >= COLS or
12                word[i] != board[r][c] or
13                (r, c) in path):
14                return False
15
16            path.add((r,c))
17
18            res = ( dfs(r+1, c, i+1) or
19                    dfs(r-1, c, i+1) or
20                    dfs(r, c+1, i+1) or
21                    dfs(r, c-1, i+1) )
22
23            path.remove((r,c))
24
25            return res
26
27        for r in range(ROWS):
28            for c in range(COLS):
29                if dfs(r, c, 0):
30                    return True
31        return False
32