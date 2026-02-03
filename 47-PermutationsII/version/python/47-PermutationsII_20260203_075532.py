# Last updated: 2/3/2026, 7:55:32 AM
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        curr = []
5
6        count = Counter(nums)
7
8        def backtrack():
9            if len(curr) == len(nums):
10                res.append(curr.copy())
11                return
12            
13            for num in count:
14                if count[num] > 0:
15                    curr.append(num)
16                    count[num] -= 1
17                    backtrack()
18
19                    curr.pop()
20                    count[num] += 1
21            
22        backtrack()
23        return res