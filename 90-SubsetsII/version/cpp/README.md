Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]

 
Constraints:


	1 <= nums.length <= 10
	-10 <= nums[i] <= 10


### 💡 Pattern: Backtracking with Duplicate Handling (Subsets II)
* **The Logic:** Sort the input and use `if (i > start_index && nums[i] == nums[i-1]) continue;` to skip over identical elements at the same recursion level, ensuring each subset in the result is unique.
* **Time Complexity:** O(N * 2^N) — There are 2^N possible subsets, and we spend O(N) time to copy each subset into the result list.
* **Space Complexity:** O(N) — We only store the current subset and the recursion stack, which both grow to a maximum depth of N.
