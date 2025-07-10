# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

 

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
from math import factorial

def permu(n : int, k : int) -> str:
    elem = [str(i) for i in range(1,n+1)]
    res = []
    k-=1

    for i in range(n,0,-1):
        idx = k//factorial(i-1)
        res.append(elem[idx])
        elem.pop(idx)
        k = k % factorial(i-1)

    return "".join(res)


print(permu(3,3))

# have to revise this later altho I have build intuition like we have to factorial formula and check all ranges for each digits
# let me expalin :-
# say we're given n = 3 and k = 3 means we have to print kth permuation of digits sequence [1,2,3] and we'll be storing it as string
# because say if we're given range from 0 to n, and storing as int will drop zero if its leading but we dont want that and we're returning str
# so we got our input we generated elements from 1 to n and mind it we're using 0 based indexing so lets substract k by 1 and initialise result array
# we'll go from n to 1 why? coz we building permuation from left to right, assume we have 1,2,3,4 total permuation will be 4! = 24
# say we pick 1 element now total permuation for 3 position will be 3! = 6 means for remaining 3 digits there are 6 ways for each to choose from
# ["1"*6, "2"*6, "3"*6, "4"*6] = 24, each digits has 6 possible way to choose or arrange from,
# each digit position is responsible for (i-1)! permutations of the rest
# so we can use division and modulo to select and reduce the search space at each step (means removing digit which comes in range of k and adding to result)
# Here's table for better understanding

'''

| First Digit | Remaining Digits | Permutations of Remaining | Total |
| ----------- | ---------------- | ------------------------- | ----- |
| `1`         | `[2,3,4]`        | `6` (3!)                  | 1-6   |
| `2`         | `[1,3,4]`        | `6`                       | 7-12  |
| `3`         | `[1,2,4]`        | `6`                       | 13-18 |
| `4`         | `[1,2,3]`        | `6`                       | 19-24 |

'''