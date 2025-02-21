#Input: arr = [17,18,5,4,6,1]
#Output: [18,6,6,6,1,-1]

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElem = -1
        for i in range(len(arr)-1,-1,-1):
            currElem = arr[i]
            arr[i] = maxElem
            maxElem = max(maxElem,currElem)
        return arr

# Time complexity: O(n)
# Space complexity: O(1)

        