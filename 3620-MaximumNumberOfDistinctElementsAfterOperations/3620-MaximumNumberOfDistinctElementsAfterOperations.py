# Last updated: 1/31/2026, 2:18:26 PM
import math
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        distinct_numbers = 0
        prev_number = -math.inf

        for num in nums:

            max_poss = num + k
            min_poss = num - k

            smallest_valid = max(min_poss, prev_number + 1)

            if smallest_valid <= max_poss:
                distinct_numbers += 1
                prev_number = smallest_valid
        
        return distinct_numbers