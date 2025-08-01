# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
INT_MAX = 2**31 - 1
x = -123
# x = 1534236469            # this will cause integer overflow
sign = -1 if x < 0 else 1
x = abs(x)
res = 0

while x:
    temp = x % 10
    x = x // 10

    if res > (INT_MAX - temp) // 10:
        print("Integer Overflow")
        break
    res = res*10 + temp
else:
    print(res*sign)