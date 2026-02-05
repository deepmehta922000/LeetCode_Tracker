// Last updated: 2/5/2026, 10:26:37 AM
1#include <vector>
2#include <numeric>
3#include <algorithm>
4#include <functional>
5
6using namespace std;
7
8class Solution {
9public:
10    bool makesquare(vector<int>& matchsticks) {
11        // 1. Basic Check: Sum must be divisible by 4
12        long long total_sum = accumulate(matchsticks.begin(), matchsticks.end(), 0LL);
13        if (total_sum % 4 != 0) return false;
14
15        int target = total_sum / 4;
16
17        // 2. Optimization: Sort descending
18        // Trying larger sticks first fills up sides faster and fails earlier
19        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
20
21        if (matchsticks[0] > target) return false;
22
23        // Array to store the current length of the 4 sides
24        vector<int> sides(4, 0);
25
26        return backtrack(0, target, matchsticks, sides);
27    }
28
29private:
30    bool backtrack(int i, int target, const vector<int>& matchsticks, vector<int>& sides) {
31        // Base Case: All matchsticks placed
32        if (i == matchsticks.size()) {
33            return true;
34        }
35
36        // Try placing matchstick i in each of the 4 sides
37        for (int j = 0; j < 4; j++) {
38            if (sides[j] + matchsticks[i] <= target) {
39                
40                sides[j] += matchsticks[i];
41                if (backtrack(i + 1, target, matchsticks, sides)) {
42                    return true;
43                }
44                sides[j] -= matchsticks[i];
45            }
46        }
47
48        return false;
49    }
50};