# Last updated: 2/8/2026, 1:42:37 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        col = set()
4        negDiag = set()
5        posDiag = set()
6
7        res = []
8
9        board = [["."] * n for i in range(n)]
10
11        def backtrack(r):
12            if n == r:
13                copy = ["".join(r) for r in board]
14                res.append(copy)
15                return
16
17            for c in range(n):
18                if ( c in col or 
19                    (r+c) in posDiag or
20                    (r-c) in negDiag ):
21                    continue
22                
23                col.add(c)
24                negDiag.add(r-c)
25                posDiag.add(r+c)
26                board[r][c] = "Q"
27
28                backtrack(r+1)
29
30                col.remove(c)
31                negDiag.remove(r-c)
32                posDiag.remove(r+c)
33                board[r][c] = "."
34
35        backtrack(0)
36        return res
37
38
39            
40
41
42
43