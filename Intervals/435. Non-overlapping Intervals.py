# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number
# of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

pairs = [[1,2],[2,3],[3,4],[1,3]]

pairs.sort(key = lambda x: x[1])
print(pairs)
prev_end, count = float('-inf'), 0

for pair in pairs:
    if pair[0] < prev_end:
        count+=1
    else:
        prev_end = pair[1]

print(count)

# Notes and Explanation

# Again Interval oh gawwwd when i'll have real interval in my life, enough with bs lets get started
# so we have to count number of overlapping intervals we can do by sorting intervals on basis of
# 2nd element in individual range given, after sorting our given intervals will look like this
# [[1, 2], [2, 3], [1, 3], [3, 4]] for above eg, now we'll compare if current pair 1st element is
# less than prev_end, think it like two pointers moving when specific conditions met, and if 
# current pair's 1st element is less than previous means current pair should 'ave been part of
# previous pair and we'll increase count not prev_end since we didnt find new interval and in case
# we did find one i.e pair[0] is not less than prev_end means this is start of new interval we'll
# this as prev_end.