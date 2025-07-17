# You are given an integer array nums containing distinct positive integers and an integer target.
# Determine if you can partition nums into two non-empty disjoint subsets, with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target.
# Return true if such a partition exists and false otherwise.
# A subset of an array is a selection of elements of the array.
 
# Example 1:
# Input: nums = [3,1,6,8,4], target = 24
# Output: true
# Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.

nums = [3,1,6,8,4]
target = 24   #O/P -> True
#target = 91   O/P -> False

def canPartition(nums, target):
    n = len(nums)
    def backtrack(idx, prodA, prodB, countA, countB):
        if prodA > target or prodB > target:
            return False
        if idx == n:
            return countA > 0 and countB > 0 and prodA == prodB == target
        if backtrack(idx+1, prodA*nums[idx], prodB, countA+1, countB):
            return True
        if backtrack(idx+1, prodA, prodB*nums[idx], countA, countB+1):
            return True
        return False
    return backtrack(0,1,1,0,0)

print(canPartition(nums, target))


# Notes and Explaination
# first of all what i originally thought of this 
'''
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        prod =  1
        for num in nums:
            prod*=num
        return prod//target == target    

'''
# and suprisingly it passed 714/720 test cases😭😭 I know this is dumb but okay
# now from the problem itself its obvious we can use recursion / backtracking if asked something like subset(from the tags😉)
# so our main idea is to at each element we'll include it now or exclude it and store product somewhere to tarck that it doesnt exceed our target
# also for comparison and so we'll backtrack first after putting that element into subset A and then into subset B, at each step we'll update
# index, prod of A and B and also count of A and B. why? coz we dont want empty set as question said.

# In simple term, lets element 1 put into A or put into B but we cant put same element in both(disjoint set) and if index in equals to length of nums
# we'll check that if countA and B are greater than zero, and prodA equals to target equals to prod B then we return True


nums1 = [3,1,6,8,4]
target1 = 24   #O/P -> True
#target = 91   O/P -> False

def partitionArr(nums1, target1):
    def backtrack(idx, prodA, prodB, countA, countB):
        if idx == len(nums1):
            return countA > 0 and countB > 0 and prodA == prodB == target1
            
        elem = nums1[idx]

        if backtrack(idx+1, prodA*elem, prodB, countA+1, countB):
            return True
        
        if backtrack(idx+1, prodA, prodB*elem, countA, countB+1):
            return True
        return False
    return backtrack(0,1,1,0,0)

print(partitionArr(nums1, target1))

# Review:-
# - i didnt handle base case successfully i was supposed to return countA > 0 and countB > 0 and prodA == prodB == target
# - but i put this in if condition and was returning true but forgot to return false if this wasnt true!
# - and i also forgot to implement early pruning, if prodA or prodB > target return false

# Points to remember 
# - make choice either include or exclude, recursively
# - count elements you've added to both subset A and B
# - base condn if index exceeds length of array or index == length + 1 check if any
# - of subsets is not empty and both subset's product are equal and equals to the target return true else false