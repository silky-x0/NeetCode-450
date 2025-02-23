# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# do this by modifying the input array in-place with O(1) extra memory.

#time complexity: O(n)
#space complexity: O(1)

def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1


# Approach 2: Two Pointers, Iteration            