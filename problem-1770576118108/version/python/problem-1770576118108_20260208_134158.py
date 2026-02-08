# Last updated: 2/8/2026, 1:41:58 PM
1class Solution:
2    
3    def totalNQueens(self, n: int) -> int:
4        col = set()
5        posDiag = set()
6        negDiag = set()
7        #self.res = 0
8        # also acceptable
9        res = [0]
10
11        def backtrack(r):
12            if r == n:
13                #self.res += 1
14                res[0] += 1
15                return
16            
17            for c in range(n):
18                if( c in col or
19                    (r+c) in posDiag or
20                    (r-c) in negDiag):
21                    continue
22                
23                col.add(c)
24                posDiag.add(r+c)
25                negDiag.add(r-c)
26
27                backtrack(r+1)
28
29                col.remove(c)
30                posDiag.remove(r+c)
31                negDiag.remove(r-c)
32
33        backtrack(0)
34        #return self.res
35        return res[0]
36