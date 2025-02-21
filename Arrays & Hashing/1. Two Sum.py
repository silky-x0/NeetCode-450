# Who doesn't know about this problem!
# Even Non-tech background people know about this problem, or at least just name of it.(iykyk)

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[num] = i

# Uses Hashing/hapmap(you may call) to store the elements as key and their indices as value in Dict.