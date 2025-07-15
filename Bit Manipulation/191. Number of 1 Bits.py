# Given a positive integer n, write a function that returns the number of set bits in its binary representation 
# (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

n = 11
count = 0
while n:
    n &= n - 1  # This operation reduces the number of set bits by one
    count += 1

print(count)  # Output: 3

# Notes and Explanation:
# The operation `n &= n - 1` clears the least significant set bit of `n`.
# The loop continues until `n` becomes zero, counting how many times we can clear a set bit.
# This is an efficient way to count the number of set bits in an integer.
# for example, for n = 11 (binary 1011) and n-1 = 10 (binary 1010)
# '&' operration says 1011 & 1010 = 1010, which clears the least significant bit.
# The process continues until all bits are cleared, counting the number of iterations.