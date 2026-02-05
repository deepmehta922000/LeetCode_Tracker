// Last updated: 2/5/2026, 10:28:13 AM
1class Solution {
2public:
3    bool makesquare(vector<int>& matchsticks) {
4        // 1. Basic Check: Sum must be divisible by 4
5        long long total_sum = accumulate(matchsticks.begin(), matchsticks.end(), 0LL);
6        if (total_sum % 4 != 0) return false;
7
8        int target = total_sum / 4;
9
10        // 2. Optimization: Sort descending
11        // Trying larger sticks first fills up sides faster and fails earlier
12        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
13
14        if (matchsticks[0] > target) return false;
15
16        // Array to store the current length of the 4 sides
17        vector<int> sides(4, 0);
18
19        return backtrack(0, target, matchsticks, sides);
20    }
21
22private:
23    bool backtrack(int i, int target, const vector<int>& matchsticks, vector<int>& sides) {
24        // Base Case: All matchsticks placed
25        if (i == matchsticks.size()) {
26            return true;
27        }
28
29        // Try placing matchstick i in each of the 4 sides
30        for (int j = 0; j < 4; j++) {
31            if (sides[j] + matchsticks[i] <= target) {
32                
33                sides[j] += matchsticks[i];
34                if (backtrack(i + 1, target, matchsticks, sides)) {
35                    return true;
36                }
37                sides[j] -= matchsticks[i];
38            }
39        }
40
41        return false;
42    }
43};