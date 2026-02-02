// Last updated: 2/2/2026, 9:16:33 AM
1class Solution {
2public:
3    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
4
5        sort(nums.begin(), nums.end());
6        vector<vector<int>> res;
7        vector<int> curr;
8
9        backtrack(nums, res, curr, 0);
10        return res;
11        
12    }
13
14private:
15    void backtrack(vector<int>& nums, vector<vector<int>>& res, vector<int>& curr, int start_index){
16        res.push_back(curr);
17
18        for (int i = start_index; i < nums.size(); i++ ){
19
20            if (i > start_index && nums[i] == nums[i-1]){
21                continue;
22            }
23
24            curr.push_back(nums[i]);
25            backtrack(nums, res, curr, i+1);
26            curr.pop_back();
27        }
28    }
29};