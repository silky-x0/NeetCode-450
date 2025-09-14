# You are given an integer array height of length n. There are n vertical lines drawn such that the two 
# endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max 
# area of water (blue section) the container can contain is 49.

h = [1,8,6,2,5,4,8,3,7]

i, j = 0, len(h) - 1
mWater = -1

while i <= j:

    area = (j-i)*min(h[i], h[j])
    mWater = max(area, mWater)
    if h[i] < h[j]:
        i+=1
    else:
        j-=1

print(mWater)

# Notes:-
# > Water is limited by shorter side so whichever side is shorter will be 
#   limiting factor and we have to move that while calulating water between i and j.