# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

nums = [1,1,2,3,3,4,4,8,8]
i,j = 0, len(nums)-1
while i<j:
    mid = (i+j) // 2
    if mid%2==0:
        if nums[mid] == nums[mid+1]:
            i = mid + 2
        else:
            j = mid
    else:
        if nums[mid] == nums[mid-1]:
            i = mid +1
        else:
            j = mid -1
print(nums[i])

#Alternate Solution

def singleNonDuplicate(self, nums: List[int]) -> int:
    i,j = 0, len(nums)-1
    while i<j:
        mid = (i+j)//2
        if nums[mid] == nums[mid^1]:
            i = mid+1
        else:
            j = mid
    return nums[i]

#Asked GPT how it works,
# 🎯 But how does it help in our binary search?
# Let’s say we are at some index mid.

# We want to find out the pair of nums[mid] — is it mid + 1 or mid - 1?

# Now comes the XOR trick:

# mid ^ 1
# It does this:

# If mid is even → mid ^ 1 = mid + 1

# If mid is odd → mid ^ 1 = mid - 1

# 🤯 Why?
# mid ^ 1 flips the last bit of mid

# Even number (last bit = 0): flipping it makes it odd (adds 1)

# Odd number (last bit = 1): flipping it makes it even (subtracts 1)

# 💡 Use in binary search
# So now, instead of writing two separate conditions like:

# if mid % 2 == 0:
#     if nums[mid] == nums[mid + 1]: ...
# else:
#     if nums[mid] == nums[mid - 1]: ...
# We just write:

# if nums[mid] == nums[mid ^ 1]:
#     # the pair is good → search right
# else:
#     # the pair is broken → search left
# ✅ Summary of XOR Trick:
# mid	mid ^ 1	Why?
# even	mid + 1	check the pair to the right
# odd	mid - 1	check the pair to the left

# This makes the code shorter, cleaner, and easier to manage.

