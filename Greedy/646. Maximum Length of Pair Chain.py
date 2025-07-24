# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

# Example 1:
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].

# Constraints:
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000

pairs = [[1,2],[7,8],[4,5]]

def maxLenChain(pairs):
    if not pairs:                             # LOL I forgot to add this, I remembered when I was explaining below
        return 0
    pairs.sort(key = lambda x: x[1])
    chain = 0
    prev_end = -1001
    for pair in pairs:
        if prev_end < pair[0]:
            chain+=1
            prev_end = pair[1]

    return chain

print(maxLenChain(pairs))

# Notes and Explanation

# We're given some pairs and we have to form chain of max Length by join two or more pairs, this question
# feels like interval to me where merge condition are less strict, like we can combine/merge pair if
# prev pair end with such number that is less than current pair starting number, now since it comes to this
# we'll be little greedy how we approach solution lets say we want max length so i can sort pairs as such
# that there is possibility to build max length of chain and we can do that by sorting based on last element 
# of each pair in increasing order, such it will provide us sufficient way to compare since we only have condition to
# check current pair 1st element with previous pair last element, and every time we say oh we macthed pair with condition
# we can increasing our chain count and updating end value with current pair's last element

# Edge cases:- 
# - Duplicate pairs -> since we dont need em we can skip 'em
# - Single pair input -> our current solution can handle single pair
# - Empty Input -> we'll return 0 if its not input/ input is empty

# Key Points:-
# - sort paris based on 2nd element in pair
# - increase chain count if condition satisfies  