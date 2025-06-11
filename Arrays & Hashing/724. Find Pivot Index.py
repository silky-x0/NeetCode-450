def pivotIndex(self, nums: List[int]) -> int:
    n = len(nums)
    sumLeft = [1] * n

    prefix = 1
    for i in range(n):
        sumLeft[i] = prefix
        prefix+=nums[i]

    sumRight = [1] * n
    suffix = 1
    for i in range(n-1,-1,-1):
        sumRight[i] = suffix
        suffix+=nums[i]

    for i in range(n):
        if sumLeft[i] == sumRight[i]:
            return i
    else:
        return -1
    
#Alternate solution
def pivotIndex(self, nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num

    return -1    