# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

def mPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1/mPow(x,-n)
    half = mPow(x, n//2)
    if n & 1 == 0:
        return half*half
    return half*half*x

print(mPow(2.000, 10))

#this has logarthimic time complexity coz on each recursion call we're dividing number by 2, so TC - O(logn)