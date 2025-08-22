# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri),
# remove all intervals that are covered by another interval in the list.
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
# Return the number of remaining intervals.

# Example 1:
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

intervals = [[1,4],[3,6],[2,8]]

intervals.sort(key=lambda x: (x[0], -x[1]))
count, right = 0, 0

for (start, end) in intervals:
    if end <= right:
        count += 1
    else:    
        right = end

print(len(intervals) - count)

# Notes and Explanation
# Core idea is to sort the intervals by starting point in ascending order and by ending point in descending order
# This way, if an interval starts the same as another, the longer one comes first
# We then iterate through the sorted intervals and keep track of the maximum right endpoint seen so far
# If the current interval's end is less than or equal to the maximum right endpoint, it is covered
# Otherwise, we update the maximum right endpoint
# Finally, we return the total number of intervals minus the count of covered intervals

# this question is similar to merge intervals except we have to return count of inervals
# that survive after removing covered intervals, we're doing length of intervals - count of covered intervals

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)