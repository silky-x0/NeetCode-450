#Using dictionary data structure as hash table
#Time complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hMap = {}
        for i,num in enumerate(nums):
            if num in hMap:
                return True
            else:
                hMap[num] = i
        return False               
        



#Using set data structure
#Time complexity: O(n)

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         visit = set(nums)
#         if len(visit) != len(nums):
#             return True
#         else:
#             return False      