# Last updated: 2/5/2026, 9:20:09 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        digit_map = {
4            '2': 'abc',
5            '3': 'def',
6            '4': 'ghi',
7            '5': 'jkl',
8            '6': 'mno',
9            '7': 'pqrs',
10            '8': 'tuv',
11            '9': 'wxyz'
12        }
13
14        res = []
15        current_combination = []
16
17
18        def backtrack(index):
19
20            if len(current_combination) == len(digits):
21                res.append("".join(current_combination))
22                return
23
24            current_digit = digits[index]
25            possible_letters = digit_map[current_digit]
26
27            for letter in possible_letters:
28                current_combination.append(letter)
29                backtrack(index+1)
30                current_combination.pop()
31            
32        if len(digits) > 0:
33            backtrack(0)
34        return res
35
36
37        