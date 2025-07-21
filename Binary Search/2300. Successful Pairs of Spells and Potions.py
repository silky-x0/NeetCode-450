# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] 
# represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

res = [0]*len(spells)
potions.sort()
for i in range(len(spells)):
    l, r = 0, len(potions) - 1
    while l <= r:
        mid = (l + r)//2
        if spells[i]*potions[mid] >= success:
            res[i]+= mid - l + 1
            r = mid - 1
        else:
            l = mid + 1

print(res)

# Notes and Explanation:-
#
# Question says to return number of potions that crosses or equal to threshold(success) for each spell in spells
# A brute force method would be using two nested loops, for eachs spells we would check each potions that crosses success rate and count the append
# that would result in T.C of O(n*m) where n is number of spells and m is number of potions

# Better Approach:-
# 
# We can make use of multiplication and sorting like what if a spell works on potion then it will work all the potions greater than
# it like we dont have to check for potions greater than it we can count number of potions left and append to the numbers
# and to work that we have to sort the potions, not spells cause it'll mess up order

# Walkthrough:-
#
# we'll create result array to store number of potions worked on all spells
# we sort the potions
# and for every spell we'll do binary search
# if spell * potions[mid] >= success
# means the spell would work for all potion from mid to end,
# so we'll addd result i.e number of potions equals to mid - left + 1
# in i'th place of spell position (and we know there still can be potion left
# to count we'll add count on previous result, we'll not replace count)
# but this not gurantees that potion will not work below mid so we'll have to check again
# since spell works on mid of potions now shift right pointer to mid - 1 
# else shift left pointer to mid + 1
# That's all we got our answer! return result of print whatever