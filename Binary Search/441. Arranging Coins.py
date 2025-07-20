import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(8*n + 1) - 1) * 0.5)

sol = Solution()
print(sol.arrangeCoins(8))

# this only mathematical way of doing this problem i'll update this with Binary Search later on

# Lets do BS solution for this

n = 8
low, high, res = 0, n, 0

while low <= high:
    mid = (low + high) // 2
    coins = (mid/2) * (mid + 1)

    if coins > n:
        high = mid -1
    else:
        low = mid + 1
        res = max(res, mid)

print(res)


# Notes and Explanation

# I dont know why it is tagged easy, it should be medium if it has to be done with binary search
# It was really difficult to come up with solution unless you're genius like gauss, who gave gauss law
# which we're using here for finidings coins we needed, lets first understand gauss law and what's its need

# Gauss law - n/2*(n+1)
# this formula gives sum of natural number upto n, for mathematical proof say n = 100
# he found that if we add two number one from starting i.e 1 and one from last i.e 100 will sum to 101
# for all numbers that is choosen is this specific manner for eg- 99+2 = 101, 98+3 = 101 upto mid i.e 50+51 = 101

# Need for Gauss law in this problem
# n = 8                  
# [1,  ,  ,  ,  ]
# [1, 1,  ,  ,  ]             (kindly look at picture in problem discription for better visualisation)
# [1, 1, 1,  ,  ]
# [1, 1,  ,  ,  ]

# we're given staircase we have to fill/arrange coins and have to return max number of staircase filled
# Given n coins, the number n itself acts as an upper bound. Why?
# Because in the worst case, we can only build at most n complete rows—
# one coin per row—resulting in n rows as the maximum possible.


# To the Solution -
# Now our arsenal is ready, lets understand will that work, well calulate mid at
# and check if coins needed to fill staircase is less than given coin, means yes we can build staircase upto mid
# but we still need to find max number so we'll added max(mid, result) to result and repeat until our loop is terminated