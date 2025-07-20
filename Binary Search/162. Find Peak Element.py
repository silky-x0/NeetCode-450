# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always
# considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

nums = [1,2,3,1]

low, high = 0, len(nums)-1

while low < high:
    mid = (low + high) // 2

    if nums[mid] < nums[mid+1]:
        low = mid + 1
    else:
        high = mid

print(low)

# Notes and Explanation

# Honestly When I first saw problem I thought oke i can do it, also i did wrote code in 2 minutes but after submitting
# I figured we have to do in logn time and I did in O(N) using two pointers😭😭, while writing i thought i'm doing great, anyways

# Our core idea is to check mid: 
# - if nums[mid] < nums[mid+1], the slope is rising, so the peak must lie on the right → set low = mid + 1
# - else, we’re on a falling slope or at a peak, so the peak is on the left or at mid → set high = mid

# Why is this guaranteed? If the slope is going up, eventually it must come down, so a peak must exist on the right.
# If it's going down, the previous higher point or mid itself could be the peak.

# We assume nums[-1] = nums[n] = -inf so the ends can also be peaks.

# nums = [1,2,1,3,5,6,4]  
# low = 0, high = 6, mid = 3 , now mid of nums i.e 3 is less than its next element(5) means peak is on right
# low = mid + 1 = 4, high = 6, mid = 5, now mid of nums is 5 which is less than its next element i.e 6
# low = 5, high = 6, mid = 5, nums[mid] = 6 which is greater than nums[mid+1] i.e 4
# low = 5, high = 5, our loop will break here and we can return either low or high since both are equal
