# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

#Recursive Approach

def searchInsert(self, nums: List[int], target: int) -> int:
        
    def binSearch(left,right,target):
        if left > right:
            return left
        mid = (left + right)//2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binSearch(left,mid-1,target)  
        elif nums[mid] <  target:
            return binSearch(mid+1,right,target)

    return binSearch(0,len(nums)-1,target)


#Iterative approach

def binSearchIterative(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left            