# Last updated: 2/9/2026, 8:50:33 AM
1class Solution:
2    def islandPerimeter(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        visit = set()
5
6        def dfs(i, j):
7            if i <0 or j < 0 or i>= rows or j >= cols or grid[i][j] == 0:
8                return 1
9            if (i,j) in visit:
10                return 0
11            
12            visit.add((i,j))
13            perimeter = dfs(i, j + 1) + dfs(i + 1 ,j) + dfs(i - 1, j) + dfs(i, j - 1)
14            return perimeter
15        
16        for i in range(rows):
17            for j in range(cols):
18                if grid[i][j]:
19                    return dfs(i,j)
20        return 0