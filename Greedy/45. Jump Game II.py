# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

nums = [2,3,1,1,4]
jump, farthest, curr_end = 0, 0, 0
for i in range(len(nums)-1):
    farthest = max(farthest, i+nums[i])
    if i == curr_end:
        jump+=1
        curr_end = farthest
        if curr_end >= len(nums) - 1:              #this was not in my original code, i came up this idea while i was writing notes below( explaining works ig).
            break
print(jump)

# Notes and Explanation
# Well well well, this problem is same as jump game 1 except here we have to find total number of jump to reach end
# and in jump game 1 we have to find if end is reachable, which is fixed here means we have to find jumps
# so we can skip i > farthest check, LOL
# anyways main idea is that we'll keep track of current position which will be farthest when starting of loop dont worry let me explain
# so thing is we'll keep track of our frog's current position and maximum it can jump from each position, so if our "i" loop variable reaches
# current position it can tell frog, you need to jump to farthest(max jump known)
# altho our frog can reach from index[1] to 4 we can stop traversal!