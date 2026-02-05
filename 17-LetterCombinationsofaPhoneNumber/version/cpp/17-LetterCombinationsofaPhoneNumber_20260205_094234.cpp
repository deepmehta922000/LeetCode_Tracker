// Last updated: 2/5/2026, 9:42:34 AM
1class Solution {
2public:
3    // Moved these to private members so backtrack can see them
4    vector<string> res;
5    vector<string> digitToChar = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
6
7    vector<string> letterCombinations(string digits) {
8        res.clear(); // Clear for multiple test cases
9        if (digits.empty()) return res;
10
11        string current = "";
12        backtrack(0, current, digits);
13        return res;
14    }
15
16private:
17    void backtrack(int index, string& current, const string& digits) {
18        // Base case: check the index, not the string itself
19        if (index == digits.size()) {
20            res.push_back(current);
21            return;
22        }
23
24        // Get letters for the current digit
25        string chars = digitToChar[digits[index] - '0'];
26        
27        for (char c : chars) {
28            current.push_back(c);           // Choose
29            backtrack(index + 1, current, digits); // Explore
30            current.pop_back();             // Un-choose (Backtrack)
31        }
32    }
33};