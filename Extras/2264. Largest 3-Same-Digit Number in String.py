# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
# Note:
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
 

# Example 1:
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".

# Example 2:
# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
nums = "6777133339"

max_digits = -1
for i in range(len(nums)-2):
    if nums[i] == nums[i+1] == nums[i+2]:
            max_digits = max(max_digits, int(nums[i]))
print("" if max_digits == -1 else str(max_digits)*3)