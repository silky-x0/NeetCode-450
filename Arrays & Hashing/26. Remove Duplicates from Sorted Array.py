#Have to return unique element, will fix rest later

from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1=Counter(nums).keys()
        i=0
        for num in nums1:
            nums[i] = num
            i+=1

        return len(nums1)