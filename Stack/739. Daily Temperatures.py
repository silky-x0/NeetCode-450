# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is
# the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is
# possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

garmi = [73,74,75,71,69,72,76,73]   # temperatures, am not gonna write this long word everywhere😭

stack = []
ans = [0] * len(garmi)

for i in range(len(garmi)-1, -1, -1):
    while stack and garmi[stack[-1]] <= garmi[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] - i
    stack.append(i)

print(ans)

# Notes and Explanation🥰

# So our approach is based on next greater element problem, if you didnt do that solve that first
# but anyways I myslef didn't solve that question but rather variant of that question in our class
# we were asked to replace element with just next greater element, so that's that ummm here in this 
# question we're traversing right to left to keep track of greater element using stack to be specific
# monotonic stack for fella's who dont know what "Monotonic stack" is, its just simple stack where we
# keep elements in specific order in stack either increasing or decreasing, here we're maintaining stack
# with temperature higher than current and storing indices instead of values which helps evaluate
# amount of days between lower and greater temperatures.

# Flow :-

# Traversing right to left we'll check if recent temperature(in stack) is less than current temprature if
# yes we'll keep poping until stack is empty of temprature greater than current is found
# if found means stack is not empty and recent element i.e stack[-1] is greater so we'll compute difference of days
# between those two and assign to answer array on that current day
# and lastly we'll append current temperature means we're done dealing with it.


# Now im gonna solve that next greater element question💃