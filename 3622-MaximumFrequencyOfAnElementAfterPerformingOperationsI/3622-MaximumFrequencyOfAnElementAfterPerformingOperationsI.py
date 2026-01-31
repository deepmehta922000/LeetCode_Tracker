# Last updated: 1/31/2026, 2:18:24 PM
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        max_val_in_nums = max(nums) if nums else 0

        max_possible_value = max_val_in_nums + k + 2

        freq_map = [0] * max_possible_value
        prefix_sum = [0] * max_possible_value

        for num in nums:
            freq_map[num] += 1
        
        for i in range(1,max_possible_value):
            prefix_sum[i] = prefix_sum[i-1] + freq_map[i]

        max_freq_found = 0

        for target_value in range(max_possible_value - 1):
            right_bound = min(max_possible_value - 1, target_value + k)
            left_bound = max(0, target_value - k)

            already_at_target = freq_map[target_value]

            nums_before_left = prefix_sum[left_bound - 1] if left_bound > 0 else 0
            nums_on_right = prefix_sum[right_bound]

            numbers_in_range = nums_on_right - nums_before_left

            nums_who_need_ops = numbers_in_range - already_at_target

            we_can_add = min(numOperations, nums_who_need_ops)

            current_total_freq = already_at_target + we_can_add

            max_freq_found = max(max_freq_found, current_total_freq)
        
        return max_freq_found

























        
        # # We need to know the max possible value we might have to check
        # max_val_in_nums = max(nums) if nums else 0
        
        # # We need to check for numbers up to max_val + k.
        # # We add +2 as a safety padding for 0-indexing and range queries.
        # max_possible_value = max_val_in_nums + k + 2
        
        # # freq_map[i] = how many numbers are *exactly* at value 'i'
        # freq_map = [0] * max_possible_value
        
        # # prefix_sum[i] = how many numbers are *at or below* value 'i'
        # prefix_sum = [0] * max_possible_value

        # # First, build the simple frequency map
        # for num in nums:
        #     freq_map[num] += 1

        # # Now, build the prefix_sum (running total) from the freq_map
        # for i in range(1, max_possible_value):
        #     prefix_sum[i] = prefix_sum[i - 1] + freq_map[i]

        
        # max_freq_found = 0
        
        # # We only need to check up to the highest number we can possibly create
        # for target_num in range(max_possible_value - 1):
            
        #     # --- Find the "catchment range" ---
        #     # People at 'target_num' can come from the range [left_bound, right_bound]
        #     left_bound = max(0, target_num - k)
        #     right_bound = min(max_possible_value - 1, target_num + k)

        #     # 1. How many people are *already at* the target? (No op needed)
        #     already_at_target = freq_map[target_num]

        #     # 2. How many people are *in the total range* [left, right]?
        #     #    We use our prefix_sum for a fast O(1) lookup.
        #     count_at_right = prefix_sum[right_bound]
        #     count_before_left = prefix_sum[left_bound - 1] if left_bound > 0 else 0
        #     in_range = count_at_right - count_before_left
            
        #     # How many people *need* an operation (a "bus pass")?
        #     who_need_ops = in_range - already_at_target
            
        #     # How many can we *actually* bring? We can't use more ops than we have.
        #     we_can_add = min(numOperations, who_need_ops)

        #     # The final frequency for this target_num is:
        #     current_total_freq = already_at_target + we_can_add
            
        #     # Update our overall best
        #     max_freq_found = max(max_freq_found, current_total_freq)

        # return max_freq_found





        