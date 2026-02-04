// Last updated: 2/4/2026, 8:20:02 AM
1class Solution {
2public:
3    vector<vector<string>> partition(string s) {
4        vector<vector<string>> res;
5        vector<string> current_partition;
6
7        backtrack(s, res, current_partition, 0 );
8        return res;
9    }
10
11private:
12    void backtrack(string s, vector<vector<string>>& res, vector<string>& current_partition, int start_index ){
13        if (start_index >= s.length()){
14            res.push_back(current_partition);
15        }
16
17        for (int end = start_index; end < s.length(); end++){
18            if(isPalindrome(s, start_index, end)){
19                current_partition.push_back(s.substr(start_index, end - start_index + 1));
20                backtrack(s, res, current_partition, end + 1 );
21                current_partition.pop_back();
22            }
23        }
24    }
25
26    bool isPalindrome(const string& s, int l, int r){
27        while (l < r){
28            if(s[l] != s[r]){
29                return false;
30            }
31            l++;
32            r--;
33        }
34        return true;
35    }
36};