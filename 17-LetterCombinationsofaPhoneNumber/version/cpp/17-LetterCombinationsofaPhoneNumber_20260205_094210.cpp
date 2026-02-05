// Last updated: 2/5/2026, 9:42:10 AM
1class Solution {
2public:
3    vector<string> res;
4    vector<string> digitToChar = {"", "", "abc", "def", "ghi", "jkl",
5                                  "mno", "qprs", "tuv", "wxyz"};
6    vector<string> letterCombinations(string digits) {
7    
8        if(digits.empty()) return res;
9        backtrack(0, "", digits );
10        return res;
11    }
12
13    void backtrack(int index, string current_substring, string &digits){
14        if(current_substring.size() == digits.size()){
15            res.push_back(current_substring);
16            return;
17        }
18
19        string chars = digitToChar[digits[index] - '0'];
20        for(char c : chars){
21            current_substring.push_back(c);
22            backtrack(index + 1, current_substring, digits );
23            current_substring.pop_back();
24        }
25    }
26};