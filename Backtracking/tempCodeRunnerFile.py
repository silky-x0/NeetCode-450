nums = [3,1,6,8,4]
# target = 24   #O/P -> True
# #target = 91   O/P -> False

# def canPartition(nums, target):
#     n = len(nums)
#     def backtrack(idx, prodA, prodB, countA, countB):
#         if prodA > target or prodB > target:
#             return False
#         if idx == n:
#             return countA > 0 and countB > 0 and prodA == prodB == target
#         if backtrack(idx+1, prodA*nums[idx], prodB, countA+1, countB):
#             return True
#         if backtrack(idx+1, prodA, prodB*nums[idx], countA, countB+1):
#             return True
#         return False
#     return backtrack(0,1,1,0,0)

# print(canPartition(nums, target))