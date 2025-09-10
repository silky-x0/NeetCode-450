#                                  |"""|                    
#                                  |___|                    
#              |"""|~~~~~~~~~~~~~~~|"""||"""|~~~~~|"""|     
#              |___|               |___||___|     |___|     
#    |"""|~~~~~|"""||"""|~~~~~|"""||"""||"""||"""||"""||"""|
#    |___|     |___||___|     |___||___||___||___||___||___|
#  0   1    0    2    1    0    1    3    2    1    2    1   

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
# 6 units of rain water (blue section) are being trapped.

h = [0,1,0,2,1,0,1,3,2,1,2,1]

l, r = 0, len(h) - 1 
lMax, rMax = h[l], h[r]
res = 0

while l < r:
    if lMax < rMax:
        l += 1
        lMax = max(lMax, h[l])
        res += lMax - h[l]
    else:
        r -= 1
        rMax = max(rMax, h[r])
        res += rMax - h[r]

print(res)

# Notes And Explanation (Will add later) 
# This is optimal solution there exist solution with liner time space complexity
# where we pecomputes left and right max for each element in separate array, then
# for each element we find water it stores using formula water at arr[i] = min(leftMax[i], rightMax[i]) - arr[i]
# why minimum? because minimum boundary is limiting factor(obviously water will overflow).

# Approach :- 
# We'll be using two pointers at extremes of array and for each element i we'll calculate
# water it stores once at a time for left or rght, which depends upon which is smaller, why?
# as I told above left max will act as limiting factor as long as we know right Max is greater than
# current left Max, and for each element we'll calculate water trapped by doing left max - arr[i]
# assume water is filled at certain level i.e left max and we need to remove solid from it i.e current element
# arr[i] after removing that we get know volume/total water trapped.

# Intuition:-
# Think of pouring water into a U-shaped valley:
#  - If the left wall is shorter than the right wall, the water spills over the left side first.
#  - That means any water depth inside is entirely decided by the left wall height — you can ignore
#    the right wall’s exact height as long as it’s taller.

# GPT Gave me this:-
# Think about the boundaries
# Imagine the bars between l and r
# If lMax < rMax, then:
# The lowest possible water level for any position between l and r is at least lMax.
# The right boundary is guaranteed to be at least rMax, which is taller than lMax.
# That means for position l+1, the real water level is determined by the shorter side, which is lMax — not 
# the unknown “max to the right.”
# So min(max_left, max_right) simplifies to lMax for this position.
# If rMax <= lMax, the mirror reasoning applies:
# For the current right side, the left boundary is taller (lMax), so the right side’s height (rMax) is the limiter.

# Why we don’t miss a “bigger max later”
# Your worry:
# “What if there’s a taller bar somewhere inside, so max_right for this index isn’t actually rMax?”
# That doesn’t break the logic, because:
# When we process the left pointer, we only do it when we already know the right boundary is taller.
# Even if rMax isn’t the tallest possible to the right, it’s already taller than lMax, so it won’t limit water on the left side.
# You don’t need the exact max_right value — just the fact it’s taller than lMax is enough.