# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

nums = [1,2,3,1]
k = 3

seen = {}

for i, num in enumerate(nums):
    if num in seen and abs(seen[num] - i) <= k:
        print("True")
        break
    else:
        seen[num] = i
else:
    print("False")

# Notes and Explanation

# I know problem discription might be confusing but in simple terms problem is asking duplicate elements with range of k(inclusive)
# My first approach was to map all value to indices and compare if any comes with range of k i'll return true but we're dealing
# with duplicates element and duplicates key arent allowed more like it'll overwrite previous key, I also thought of using
# list of list but it'll become then n^2 TC cause of array lookup inside another loop
# In above approach we'll be using dictionary or hashmap for efficient lookups and addition of new element
# and update duplicates element with most recent seen index because when next duplicates comes we can check if current
# abs(index - last) index is less or equal to k or not if yes return true if not update recent index with last seen
