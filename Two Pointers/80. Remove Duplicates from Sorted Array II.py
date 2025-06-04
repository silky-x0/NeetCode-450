# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# Return k after placing the final result in the first k slots of nums.

def removeDuplicates(nums:list[int]) -> int:
    size = len(nums)
    if size == 1:
        return 1
    if size == 2:
        return 2
    i,j = 2,2
    while j < size:
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i+=1
            j+=1
        else:
            j+=1

    return i


nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
print(nums)