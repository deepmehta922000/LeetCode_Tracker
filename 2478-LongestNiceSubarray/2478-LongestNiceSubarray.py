# Last updated: 1/31/2026, 2:18:39 PM
# class Solution:
#     def longestNiceSubarray(self, nums: List[int]) -> int:
#         bitwise = []
#         count = 0
#         longest = 1
#         for i in range(len(nums)-1):
#             if (nums[i] & nums[i+1] == 0):
#                 bitwise.append(1)
#                 count += 1
#                 print(count)
#             else:
#                 bitwise.append(0)
#                 count = 0
#             if longest < count:
#                     longest = count
#         return(longest)



#         # if(sum(bitwise) == 0):
#         #     return 1
#         # else:
#         #     return sum(bitwise)
            
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        used_bits = 0  # Tracks bits used in current window
        window_start = 0  # Start position of current window
        max_length = 0  # Length of longest nice subarray found

        for window_end in range(len(nums)):
            # If current number shares bits with window, shrink window from left
            # until there's no bit conflict
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[
                    window_start
                ]  # Remove leftmost element's bits
                window_start += 1  # Shrink window from left

            # Add current number to the window
            used_bits |= nums[window_end]

            # Update max length if current window is longer
            max_length = max(max_length, window_end - window_start + 1)

        return max_length