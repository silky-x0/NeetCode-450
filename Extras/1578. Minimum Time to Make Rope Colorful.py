# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color,
# so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 
# 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.

# Example 1:
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.

def minCost(self, c: str, t: List[int]) -> int:
    res = j = 0
    for i in range(1,len(c)):
        if c[i] == c[j]:
            res += min(t[i], t[j])
            if t[i] > t[j]:
                j = i
        else:
            j = i        
    return res

# Notes:
# We iterate through the string of colors while keeping track of the last balloon's index (j).
# When we find two consecutive balloons of the same color, we add the minimum removal time to the result.
# We then update j to the index of the balloon with the higher removal time, ensuring we always keep the one that costs more to remove.
# This continues until we have processed all balloons, and we return the total minimum time required to make the rope colorful.
# 
# The time complexity of this solution is O(n), where n is the length of the colors string, as we make a single pass through the string.