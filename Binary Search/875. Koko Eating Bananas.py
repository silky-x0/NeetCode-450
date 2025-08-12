# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas,
# she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

piles = [30,11,23,4,20]
h = 5

def canFinish(k):
    return sum((p + k - 1)//k for p in piles ) <= h
    # or
    # hours = 0
    # for p in piles:
    #     hours+=(p+k-1) / k
    # return hours <= h

i, j = 1, max(piles)
while i <= j:
    mid = (i+j) // 2
    if canFinish(mid):
        j = mid - 1
    else: i = mid + 1

print(i)

# Notes and Explanation
# In this question koko a dumb monkey(like us) wants to eat banana and there is a guard which leaves all piles for certain 
# h hours[ from test cases I came know at some point this guard leaves piles for 823855818 hours😭, why bro why?] umm anyways
# so we need to find speed of koko's eating banana i.e K banana per hour so that koko can finish all piles before guard comes
# and and koko cant change piles in mid hours, say if k = 4 banana / hour, 1st pile has 3 banana it cant move to next pile
# means if piles[i] <= k, time taken to eat that pile will be `k` not less than that.

# Approach
# Our Idea is that we'll take some speed k and test if koko can finish given piles or not, and for range minimum and max speed
# will 1 and max(piles) respectively, because koko cant eat half banana and max will max of all piles[]
# because even if she ate faster, she’d still be limited to finishing that pile in 1 hour.
# so our problems becomes find the smallest k where she finishes in k ≤ h hours becomes a monotonic
# condition check → Binary Search is the efficient choice.
# Now we can simple use Binary search with our canFinish Helper function to solve this problem