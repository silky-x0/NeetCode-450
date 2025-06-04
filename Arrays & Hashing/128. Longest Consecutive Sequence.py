# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

def LongestConSeq(nums:list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in numSet:                          #O(n) traversal
        if n-1 not in numSet:                 #O(1) for lookup
            length = 1
            while n+length in numSet:         #O(1) fr lookup
                length+=1
            longest = max(length, longest)

    return longest            


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(LongestConSeq(nums))


#Time complexity :- O(n) + O(1) O(1) = O(n)