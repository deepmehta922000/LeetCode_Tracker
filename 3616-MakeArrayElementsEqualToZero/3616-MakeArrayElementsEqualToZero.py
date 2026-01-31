# Last updated: 1/31/2026, 2:18:27 PM
from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_starts = 0
        
        # 1. Get the total number of "bounces" required to clear the board.
        total_bounces_required = sum(nums) 
        
        # 2. Set up our "sliding" counters.
        # 'bounces_needed_on_left' is the sum of nums[0...i-1] (all bumpers we've passed)
        # 'bounces_needed_on_right' is the sum of nums[i+1...n-1] (all bumpers ahead)
        
        bounces_needed_on_left = 0
        # At the start (before index 0), all bounces are on the "right".
        bounces_needed_on_right = total_bounces_required

        # 3. Iterate through each cell to find launch bays ('0')
        for i in range(n):
            if nums[i] == 0:
                # --- This is a launch bay! ---
                # At this index 'i', our counters 'bounces_needed_on_left' and
                # 'bounces_needed_on_right' are now the exact totals for
                # the left and right sides of this specific launch bay.
                
                # We now check the two possible start directions:

                # --- Check 1: Can we start by moving RIGHT? ---
                # A "start right" move (1st, 3rd, 5th...) delivers the 
                # (potential) extra bounce to the right side.
                # This is a valid start if the right side needs
                # exactly 0 or 1 more bounces than the left side.
                if 0 <= bounces_needed_on_right - bounces_needed_on_left <= 1:
                    valid_starts += 1
                    
                # --- Check 2: Can we start by moving LEFT? ---
                # A "start left" move (1st, 3rd, 5th...) delivers the
                # (potential) extra bounce to the left side.
                # This is valid if the left side needs
                # exactly 0 or 1 more bounces than the right side.
                if 0 <= bounces_needed_on_left - bounces_needed_on_right <= 1:
                    valid_starts += 1
            
            else:
                # --- This is a bumper! ---
                # As we move our position 'i' one step to the right,
                # the bumper nums[i] is no longer on the "right" of us,
                # it's now on the "left". We update our totals.
                bounces_needed_on_left += nums[i]
                bounces_needed_on_right -= nums[i]
                
        return valid_starts