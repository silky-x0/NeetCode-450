# Given two integers n and k, return all possible combinations of k
# numbers chosen from the range [1, n]. You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.


def combine(n, k):
    res = []
    temp = [x for x in range(1,n+1)]
    def backtrack(idx, combination, count):
        if count == k:
            res.append(combination[:])
            return

        if idx == n:
            return

        backtrack(idx+1, combination + [temp[idx]], count+1)    
        backtrack(idx+1, combination, count)
    backtrack(0, [], 0)
    return res

print(combine(4, 2))

# Notes and Explanation 

# So this problem was similar to LC 3566 where we have to partition array into equal subsets
# only addition is we only have to create subsets with only k elements
# so just add if count or length of current combination is equal to k then added to res and result
# also check for idx.

# By the way I did lot of usless things later realised when I gave code to gpt to ask😭 
# - I didnt have to create temporay array to seacrh for subset but I can use for loop inside backtrack fxn
# - I didnt have to passs 'count' parameter we do it with length of combination

# Here the revised code :-
'''
def combine(n, k):
    result = []

    def backtrack(idx, combinations):
        if len(combinations) == k:
            result.append(combinations[:])
            return

        for num in range(idx, n+1):
            combinations.append(num)
            backtrack(num+1, combinations)
            combinations.pop()

    backtrack(1, [])
    return result

print(combine(4,2)) 

'''       
