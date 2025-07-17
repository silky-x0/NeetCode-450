# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer 
# after removing k digits from num.

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

nums = "1432219"
k = 3

stack = []

for num in nums:
    while stack and stack[-1] > num and k!=0:
        stack.pop()
        k-=1
    stack.append(num)    

while stack and k > 0:                                         # this will handle if string has one element
    stack.pop()                                                # and strings with increasing order element
    k-=1

print("".join(stack).lstrip("0") if stack else "0")

# Notes and Explanation

# core idea is to maitain stack of elements less tha current element
# let me explain we have to return string after removing k elements to make smallest string
# so what we'll do is we'll remove element from stack if cuurent element is less than last element
# in stack, why? lets understand with example say we have num = "14321" in this if we look at the index 1
# value is 4 and in thousand position(place value) so we must remove and replace that number with value smaller than 
# that and we cant do it randomly we must preserve order so, each time we'll ask if current element is greater?
# if yes pop it and decrease k(keep track over this while poping) until stack[-1] < current num and mind that
# we'll not pop if stack[-1] == num because it doesnt make our number smaller and that way we'll preserve k for future

# what if num = 12345 i.e in increasing order in that case every element will be added to stack because
# every previous element is smaller than current so to handle that we'll have to add extra step until k is not 0
# we'll keep poping from stack and return stack in string from but wait what if string has leading zeros
# simply zeros and return string here i used strip method you can also use loop for idx where zero ends
# and from that position until end return strings!


# Points to remember 
# - pop if stack[-1] is greater than current element
# - handle if k is not zero
# - handle is string has leading zeros and nums with length < k