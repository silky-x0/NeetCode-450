# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3

# Explanation:

# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

cars = list(zip(position,speed))        #zipping into one coz cars cant overtake
cars.sort(reverse=True)                 #sorting in non-increasing order, for which we'll know which car is closest to target

maxTime = 0
fleet_count = 0

for pos, spd in cars:                  
    time = (target-pos)/spd            #time to reach target
    if time > maxTime:                 
        fleet_count+=1
        maxTime = time
print(fleet_count)

# What we're doing is we're evaluationg time to reach target and starting from position which is closest
# to target we'll check if car behind is faster in terms of reaching target if yes we'll increase fleet count

#Time Complexity: O(nlogn) Space Complexity: O(n)



#Stack soln I found on submitted code

gaadi = list(zip(position,speed))        #zipping into one coz cars cant overtake
gaadi.sort(reverse=True)

s = []
for jgh, tezi in gaadi:
    s.append((target-jgh)/tezi)
    if len(s) >= 2 and s[-1] <= s[-2]:
        s.pop()

print(len(s))