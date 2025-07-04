import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(8*n + 1) - 1) * 0.5)

sol = Solution()
print(sol.arrangeCoins(8))

# this only mathematical way of doing this problem i'll update this with Binary Search later on