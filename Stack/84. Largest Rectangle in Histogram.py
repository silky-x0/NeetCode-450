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