# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


#this has time complexity of O(n)

def removeElement(nums: list[int], val: int) -> int:
    i, j = 0, 0
    while j < len(nums):
        if nums[j] != val:
            nums[i] = nums[j]
            i+=1
            j+=1
        else:
            j+=1 
    return i 

lest = [1,2,3,2,2]
valu = 2
print(removeElement(lest,valu))     
   