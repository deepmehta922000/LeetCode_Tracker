// Last updated: 2/2/2026, 9:51:42 AM
1class Solution {
2public:
3    vector<vector<int>> permuteUnique(vector<int>& nums) {
4        vector<vector<int>> res;
5        vector<int> curr;
6        unordered_map<int,int> count;
7
8        for(int& num : nums){
9            count[num]++;
10        }
11
12        backtrack(nums, res, curr, count);
13        return res;
14    } 
15
16private:
17    void backtrack(vector<int>& nums, vector<vector<int>>& res, vector<int>& curr, unordered_map<int,int>& count){
18        if(curr.size() == nums.size()){
19            res.push_back(curr);
20            return;
21        }
22
23        for(auto& [num, cnt] : count){
24            if (cnt > 0){
25                curr.push_back(num);
26                cnt--;
27                backtrack(nums, res, curr, count);
28
29                cnt++;
30                curr.pop_back();
31            }
32        }
33    }
34};