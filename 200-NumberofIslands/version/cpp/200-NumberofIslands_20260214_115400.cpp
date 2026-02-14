// Last updated: 2/14/2026, 11:54:00 AM
1class Solution {
2public:
3    int numIslands(vector<vector<char>>& grid) {
4        int ROWS = grid.size(), COLS = grid[0].size();
5        int islands = 0;
6
7        for (int r = 0; r < ROWS; r++){
8            for (int c = 0; c < COLS; c++){
9                if(grid[r][c] == '1'){
10                    dfs(grid, r, c);
11                    islands++;
12                }
13            }
14        }
15        return islands;
16    }
17
18    void dfs(vector<vector<char>>& grid, int r, int c){
19        if(r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == '0'){
20            return;
21        }
22
23        grid[r][c] = '0';
24        dfs(grid, r + 1, c);
25        dfs(grid, r - 1, c);
26        dfs(grid, r, c + 1);
27        dfs(grid, r, c - 1);
28    }
29};