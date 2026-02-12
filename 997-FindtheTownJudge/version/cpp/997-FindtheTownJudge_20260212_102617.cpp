// Last updated: 2/12/2026, 10:26:17 AM
1class Solution {
2public:
3    int findJudge(int n, vector<vector<int>>& trust) {
4        vector<int> delta(n + 1, 0);
5
6        for ( auto& t : trust){
7            delta[t[0]]--;
8            delta[t[1]]++;
9        }
10
11        for(int i = 1 ; i <= n; i++) {
12            if(delta[i] == n - 1){
13                return i;
14            }
15        }
16        return  -1;
17    }
18};