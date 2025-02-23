# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Do this in-place without making a copy of the array.

# First i thought of this approach:

def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums.pop(i))

# But this is not the correct approach because it is not in-place,
# because pop operation shifts all the elements to the left of the list
# and append operation adds the element to the right of the list.
# So, the time complexity of this approach is O(n^2).
# 
# The correct approach is to use two pointers, one for iterating the array,
#  and the other for placing the non-zero elements at the beginning of the array.
# 
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1   

# This approach has a time complexity of O(n) and space complexity of O(1).                             