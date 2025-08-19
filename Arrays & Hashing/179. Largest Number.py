# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

nums = [3,30,34,5,9]

nums = sorted(map(str, nums), key = lambda x: x*10, reverse = True)

print("".join(nums).lstrip("0") or "0")

# Notes and Explanation
# Core Idea is to sorting nums lexicographically in reverse order since we need largest number we
# won't go arounf checking all permutations of numbers and check which is greater right that would be
# O(n!*n*k), n! for all permutations and n*k for concatination of string of k numbers.

# lexicographic means order they appear in dictionary, we'll convert int to str and use key a lambda function
# that replicate and string 10 times, like we have "1" It'll provide answer "1111111111" you may ask why we doin this
# well lets take scenerio, we have "3" and "30" so when comparing normally it given [30,3] which is wrong correct
# order should be [3,30], now we're clear why we replicating strings multiple times that it to compare efficiently
# but question comes again why we choosen 10 not 2 or 3 or something, for eg [12, 121] taking 2 we'll have
# "1212" and "12121" comparing each character willl yield result ["121","12"] i.e "12112" but its not largest number
# which is supposed to be ["12", "121"] i.e "12121" .. so we multiply exactly by 10 because it as safe upper bound
# (from Question constraint i.e 0 <= nums[i] <= 10^9, 1000000000 = 10 digits or to be specific max_len)

# Now lets understand how x*10 works as key-
# we have "12" and "121" this will give "12121212121212121212" and "121121121121121121121121121121" respectively
# when comparing these will given correct order because 4th character 2 > 1 this yield [12,121] which is actually
# if we compare "12" + "121" i.e "12121" > "121" + "12" i.e "12112"

# Edge case - like [0,0]
# Handle this we used something or operator which return true value
# eg - [0,0] = "00"
# becomes "" because lstrip("0") (for leading zeros)
# we compare "" or "0"
# since "" empty string is falsy value and "0" becomes truthy (actually it is)
# so it'll print or return "0"