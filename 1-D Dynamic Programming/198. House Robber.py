nums = [6,1,2,4,8,9]

def maxRob(nums:list) -> int:
    rob1, rob2 = 0, 0
    for num in nums:
        newRob = max(rob1+num, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2

print(maxRob(nums))

#At first honestly i did got the problem i was thinking to start loop from 1 to n-2 and check back and forth
#but that has logical error and confusing
#and btw this is 2nd revision of this probelm now when trying now i can easily put intuition to
#solve w/out looking code isnt it nice!! yes it is!!    