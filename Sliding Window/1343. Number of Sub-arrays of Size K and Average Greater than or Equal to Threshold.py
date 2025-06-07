# Example 1:
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

# Example 2:
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        size = len(arr)
        if size == k:
            return 1 if sum(arr)//size >= threshold else 0
        if size < k:
            return 0


        i, j = 0, k - 1
        subArrCount = 0
        windowSum = sum(arr[i:j+1])
        while j < size:
            windowAvg =  windowSum // k
            if windowAvg >= threshold:
                subArrCount+=1
            windowSum-=arr[i]    
            i+=1  
            j+=1
            if j < size:
                windowSum+=arr[j]  

        return subArrCount

#This is what I coded in 2nd version, in 1st version I used Sum fcn inside while loop with slicing method to extract sum which leads to TLE for last test case which has time complexity of O(nk)    
#Compact version

def numOfSubArr(nums, threshold, k):
    if not nums or not k:
        return 0
    
    target = k * threshold
    windowSum = 0
    subArrCount = 0
    for i in range(k):
        windowSum+=nums[i]
    if windowSum >= target:
        subArrCount+=1

    for i in range(k,len(nums)):
        windowSum+=nums[i] - nums[i-k]
        if windowSum >= target:
            subArrCount+=1

    return subArrCount

print(numOfSubArr([2,2,2,2,5,5,5,8], 4, 3))            