# Example 1:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.

# Example 2:
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

nums =  [3,1,4,2]
second = -1                                 #initialise float(-inf) in actual problem
stack = []
for num in reversed(nums):                 #for condition i<j<k
    if num < second:                       #checking for poential first element i.e smallest
        print("True")
        break
    while stack and stack[-1] < num:       #here we are looking for the potential second element i.e greatest and storing in stack
        second = stack.pop()               #removing if we find a greater element
    stack.append(num)                      #pushing the current element to stack i.e greatest element so far
else:
    print("False")

# In simple terms we are storing the potential greatest element in the stack
# number smaller than greatest in "Second" variable
# and checking if current element is smaller than "Second" the we have found a 132 pattern

# Time Complexity: O(n)
# Space Complexity: O(n) in worst case, O(1) in best case

