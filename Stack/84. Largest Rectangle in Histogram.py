# Refer to LC I cant paste image here !

h = [2,1,5,6,2,3]

# prev smallest element [index]
stack = []
prev_smallest = [-1]*len(h)

for i in range(len(h)):
    while stack and h[stack[-1]] >= h[i]:
        stack.pop()
    if stack:    
        prev_smallest[i] = stack[-1]
    stack.append(i)

# next smallest [index]

next_smallest, stack1 = [len(h)]*len(h), []

for i in range(len(h)-1,-1,-1):
    while stack1 and h[stack1[-1]] >= h[i]:
        stack1.pop()
    if stack1:    
        next_smallest[i] = stack1[-1]
    stack1.append(i)
print(next_smallest)

max_ = -1
for i in range(len(h)):
    span = next_smallest[i] - prev_smallest[i] - 1
    max_ = max(max_, h[i] * span )

print(max_)

# Notes and Explanation:-
# To be very honest I had no idea how to solve this problem or maybe I was not going to
# solve it in a while but I saw reel about this problem where he was explaning how
# Next Greater Left and right, Next Smllest Left and right and it says If I know that
#  I can solve many problem, including this and trapping rain problem(which i'll be doing next)
# so now i got hint I applied and question becomes easy, and its core of the this problem

# Approach:-
# We'll find Next smallest left and next smallest right, by that we'll calculate span/width of current
# current rectangle.
# For each bar, we want to know:
#   1. How far we can extend to the left before hitting a shorter bar.
#   2. How far we can extend to the right before hitting a shorter bar.
# These boundaries tell us the maximum "span" this bar can be the limiting height for

# Intuition:-
# Imagine standing on top of a histogram bar and stretching your arms left and right until you 
# bump into a shorter bar. The space between those boundaries is the widest rectangle you can form 
# with that bar’s height.


# Time complexity: O(n) because each index is pushed and popped at most once from the stacks.
# Space complexity: O(n) for the stacks and NSL/NSR arrays.