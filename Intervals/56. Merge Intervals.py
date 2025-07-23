# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key = lambda x:  x[0])
res = [intervals[0]]
for curr in intervals[1:]:
    prev = res[-1]
    if curr[0] <= prev[1]:
        res[-1][1] = max(curr[1], prev[1])
    else:
        res.append(curr)
print(res)

# Notes and Explanation

# Another day nother question, umm so in this we have to merge intervals those are with overlapping boundaries
# and to check boundaries we to sort the intervals with fist element, i.e from where each interval is starting
# if we do that we can easily find which interval overlap other by just checking first element of current interval
# and last element of previous, if its overlap we'll assign max element between previous[1] and current[1] to
# the interval that is taken into account rn that is res[-1], and by the way we'll add our first interval as it is
# for comparison and all.


# Key Points :-\
# - sort the intervals based on 1st element each, i.e 0th element for 0 indexed array
# - compare previous[1] and current[0] if overlaps, replace previous[1] with max of previous[1], current[1]
# - else append array as it is since it doesnt overlap.