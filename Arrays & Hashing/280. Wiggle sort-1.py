# You are given an array ‘ARR’ containing ‘N’ integers, you need to sort the array such that a wiggle sequence is formed. A wiggle sequence satisfies the following property: ARR[0] ≤ ARR[1] ≥ ARR[2] ≤ ARR[3] ≥ ARR[4] ≤ ARR[5] …..

# If there are multiple answers, you may print any of them.
# Follow up :

# Can you try to solve this problem in O(N) time without using extra space?

# Custom Input :

# Kindly use print statements to debug the code and print array.

# Example :

# If ‘N’ = 5 and ‘ARR’ = { 1, 2, 3, 4, 5 }

# Then rearranging the input array to { 1, 4, 2, 5, 3 } create a wiggle sequence.

# Other rearrangements like { 2, 4, 3, 5, 1 }, { 3, 5, 1, 4, 2} are also considered correct.


# Description is from Naukri.com

#original solution i came up with
def wiggleSort(n, arr):
    arr.sort()     #added this later
    l = -(n // -2) #ciel division
    res = []
    for i in range(l):
        res.append(arr[i])
        if i+l < n:
            res.append(arr[i+l])
    return res


print(wiggleSort(5, [1,2,3,4,5])) 

# This solution I came up when i was making assumption, given array which is sorted and on unsorted array it
# failed so simply i add sort to top but time complexity becomes O(nlogn) sure sort() method
# and space is O(n) since its result we'll consider it but if question says true linear space
# there is another method, below


def wiggleWoggle(n, arr):
    for i in range(1, n):
        if i % 2 == 0:
            if not (arr[i-1] <= arr[i]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                if not (arr[i-1] >= arr[i]):
                    arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

print(wiggleWoggle(5, [1,2,3,4,5]))


# Ig its failrly easy to come with intuition for first one, 2nd one is also
# good but require litter more thinking.