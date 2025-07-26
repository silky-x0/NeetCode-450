# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

nums = [-2,1,-3,4,-1,2,1,-5,4]

maxLocal = maxGlobal = nums[0]                          

for num in nums[1:]:
    maxGlobal = max(maxGlobal, maxLocal + num)
    maxLocal = max(num, maxLocal + num)

print(maxGlobal)

# Notes and Explanation😎

# Here we are again, for this problem naive approach would be try to find would max sum using two loops 
# outer will run for i = 0 to n-1, we'll initialise our maxGlobal variable then comes inner loop that will run
# from i to n-1 and inside that we'll update our maxLocal with current value and check if its less than 0 we'll
# start new subarray from that point and setting maxLocal to zero outside 2nd loop we'll update our maxGlobal
# if its less then maxLocal, it has TC of n^2 which is oke because there exist a brute force approach which has n^3 TC
# so our optimal solution is using kadane's algorithm, and by the way this question comes under both Greedy and Dynamic Programming
# Our idea is simple and trivial once you look at the code, we're taking one value at a time updating global maximum and local maximum
# we're resetting local maximum to current num if curernt num + localMax is -ve, like in naive approach we're telling oke 
# new subarray should start from here.

# And follow Up question can be that instead of sum you have to print subarray that has max sum, here's the code
'''

nums = [-2,1,-3,4,-1,2,1,-5,4]    
maxLocal, maxGlobal = 0, float('-inf')
start = end = 0
temp_start = 0

for j in range(len(nums)):
    maxLocal += nums[j]
    
    if maxGlobal < maxLocal:
        maxGlobal = maxLocal
        start = temp_start                                                         <- Update the actual start
        end = j                                                                    <- Update the actual end
        
    if maxLocal < 0:
        maxLocal = 0
        temp_start = j + 1                                                         <- Next subarray starts after current position

print(f"Subarray: {nums[start:end+1]}")
print(f"Sum: {sum(nums[start:end+1])}, Max: {maxGlobal}")            

'''