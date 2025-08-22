# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false


def happyNum(n):
    if n == 1 or n == 7:
        return True
    while n > 9:
        n = sum(int(x)**2 for x in str(n))
        if n == 1 or n == 7:
            return True
    return False

print(happyNum(19))

# Notes and Explanation (will add later)
# Core idea is to use sum of squares of digits
# we will keep replacing n with sum of squares of digits until n becomes 1 or 7
# if n becomes 1 or 7 we will return True
# we are using 7 because it is the only other happy number that leads to cycle end
# eg- 7 -> 49 -> 97 -> 130 -> 10 -> 1 or 1 -> 1
# All other numbers lead to cycle or unhappy number
# eg- 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle)
# 3 -> 9 -> 81 -> 65 -> 61 -> 37 (cycle)
# 4 -> 16 -> 37 (cycle) 
# 5 -> 25 -> 29 -> 85 -> 89 (cycle)
# 6 -> 36 -> 45 -> 41 -> 20 (cycle)
# 8 -> 64 -> 52 -> 29 (cycle)
# 9 -> 81 -> 65 (cycle)





# Key points:-
# number other than 1 or 7 is unhappy, they lead to cycle
# or unhappy number