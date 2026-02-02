# Last updated: 2/2/2026, 9:40:48 AM
'''
LeetCode 47: Permutations II

Problem Description

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example:

Input: nums = [1, 1, 2]

Output: [[1,1,2], [1,2,1], [2,1,1]]

Solution Approach: Backtracking with Frequency Map

The core challenge of this problem is handling duplicate numbers to ensure that the same permutation isn't generated multiple times.

In this implementation, we use a Frequency Map (collections.Counter) instead of the traditional boolean visited array. This provides two major advantages:

Duplicate Pruning: Instead of iterating over the original nums list (which contains duplicates), we iterate over the unique keys of the Counter. This ensures that at any given position in the permutation, we only try a specific number once.

State Management: We decrement the count of a number when we include it in our current path (curr) and increment it back (backtrack) once the recursive call returns.

The Algorithm

Generate a frequency map of all numbers in the input.

Define a recursive backtrack function:

Base Case: If the length of the current path matches the length of the input, we have a complete permutation. Append a copy to the results.

Recursive Step: Iterate through the unique numbers in the frequency map. If a number has a count $> 0$, "choose" it, decrement its count, and recurse. After the recursion, "un-choose" it by incrementing the count and popping it from the path.

Complexity Analysis

Time Complexity: $O(\sum_{k=1}^{N} P(N, k))$, where $N$ is the length of the array. In the worst case (all unique elements), it is $O(N \cdot N!)$. However, with duplicates, the number of branches is significantly reduced.

Space Complexity: $O(N)$ to store the frequency map and the recursion stack.

Implementation

The implementation can be found in permute_unique_fixed.py.

from collections import Counter

def permuteUnique(nums):
    res = []
    count = Counter(nums)
    
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(list(curr))
            return
        
        for num in count:
            if count[num] > 0:
                count[num] -= 1
                curr.append(num)
                backtrack(curr)
                curr.pop()
                count[num] += 1
                
    backtrack([])
    return res
'''

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