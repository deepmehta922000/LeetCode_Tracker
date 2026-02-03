// Last updated: 2/3/2026, 8:28:24 AM
1class Solution {
2public:
3    vector<string> generateParenthesis(int n) {
4        vector<string> res;
5        string stack;
6        backtrack(0, 0, n, res, stack);
7        return res;
8    }
9
10    void backtrack(int openN, int closedN, int n, vector<string>& res, string& stack){
11        if(openN == closedN && openN == n){
12            res.push_back(stack);
13        }
14
15        if (openN < n){
16            stack += '(';
17            backtrack(openN + 1, closedN, n, res, stack);
18            stack.pop_back();
19        }
20
21        if (closedN < openN){
22            stack += ')';
23            backtrack(openN, closedN + 1, n, res, stack);
24            stack.pop_back();
25        }
26    }
27};