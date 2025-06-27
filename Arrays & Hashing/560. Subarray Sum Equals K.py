# Input: nums = [1,1,1], k = 2
# Output: 2

nums = [1,1,1]
k = 2

def subarrSumK(nums:list[int],k:int) -> int:
    prefixSum = 0
    seen = {0:1}
    count = 0
    for num in nums:
        prefixSum += num
        if prefixSum - k in seen:
            count+=seen[prefixSum-k]
        seen[prefixSum] = seen.get(prefixSum,0)+1
    return count    

print(subarrSumK(nums,k))

#have to revise this again !!!!!