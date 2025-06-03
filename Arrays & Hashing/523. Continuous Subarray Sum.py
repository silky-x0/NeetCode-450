# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.




class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: -1}  # Map to store remainder -> index
        total = 0          # Running prefix sum

        for i, num in enumerate(nums):
            total += num   # Update running sum

            if k != 0:
                total %= k  # Keep only the remainder when divided by k

            if total in mod_map:
                # Check if the subarray length is at least 2
                if i - mod_map[total] >= 2:
                    return True
            else:
                # Store the first time this remainder is seen
                mod_map[total] = i

        return False  # No valid subarray found