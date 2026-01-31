# Last updated: 1/31/2026, 2:18:36 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones_count = 0
        total_array_gcd = 0 # GCD of all elements in the array

        for x in nums:
            if x == 1:
                ones_count += 1
            total_array_gcd = math.gcd(total_array_gcd, x)

        # --- Case 1: '1's already exist ---
        # We just need to "spread" the 1s.
        if ones_count > 0:
            cost_to_spread = n - ones_count
            return cost_to_spread
        
        # --- Case 2: Impossible to make a '1' ---
        # If the GCD of the whole array is > 1 (e.g., all are even),
        # no amount of GCD operations can ever create a 1.
        if total_array_gcd > 1:
            return -1

        # --- Case 3: No '1's exist, but it's possible ---
        # We must find the *shortest subarray* that can create a '1'.
        
        shortest_subarray_len = n
        
        # O(n^2) search for the shortest subarray with a GCD of 1
        for i in range(n):
            current_subarray_gcd = 0
            for j in range(i, n):
                current_subarray_gcd = math.gcd(current_subarray_gcd, nums[j])
                
                # We found a subarray that can be reduced to 1
                if current_subarray_gcd == 1:
                    current_subarray_len = j - i + 1
                    shortest_subarray_len = min(shortest_subarray_len, current_subarray_len)
                    # We can stop this inner loop, since we
                    # found the shortest one *starting* at 'i'.
                    break 

        # --- Calculate Final Cost ---
        # The total cost is (Cost to Create 1) + (Cost to Spread 1)
        
        # It takes (length - 1) ops to reduce a subarray to a single 1.
        cost_to_create_first_one = shortest_subarray_len - 1
        
        # It takes (n - 1) ops to spread that 1 to the other elements.
        cost_to_spread = n - 1
        
        return cost_to_create_first_one + cost_to_spread