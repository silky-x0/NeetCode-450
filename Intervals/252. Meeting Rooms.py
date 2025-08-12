# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]
# (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

# Example 1:
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation:
# (0,30) and (5,10) will conflict
# (0,30) and (15,20) will conflict
import sys
intervals = [(5,10),(15,20),(0,30)]

if not intervals:
    print("True")      # edge case
    sys.exit()
intervals.sort(key = lambda x: x[0])    # for leetcode to acces first element we'll use x.start and for last x.end where x is tuple object

prev = [intervals[0][1]]   # intervals[0].end
for inter in intervals[1:]:
    if prev[-1] > inter[0]:    # inter.start
        print("False")
        break
    else: prev.append(inter[1]) # inter.end

else:
    print("True")

# Notes and Explantion 
# this question is same as overlapping intervals but twist is we're given interval object instead of tuple!
# so to access starting element use `intervalObject.start` and to access last element use `intervalObject.end`