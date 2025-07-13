# You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] 
# is the initial distance in kilometers of the ith monster from the city. The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an 
# integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute. You have a weapon that, 
# once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.
# You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and 
# the game ends before you can use your weapon. Return the maximum number of monsters that you can eliminate before you lose,
# or n if you can eliminate all the monsters before they reach the city.

# Example 1:
# Input: dist = [1,3,4], speed = [1,1,1]
# Output: 3
# Explanation:
# In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
# After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
# After a minute, the distances of the monsters are [X,X,2]. You eliminate the third monster.
# All 3 monsters can be eliminated.
import math
dist = [1,3,4]
speed = [1,1,1]

time = []
for d,s in zip(dist,speed):
    time.append(math.ceil(d/s))

time.sort()    
for minute in range(len(time)):
    if time[minute] <= minute:
        print(minute)
        break
else:
    print(len(time))


# Notes and Explanation 🥰

# Everytime you see distance and speed, evaluate time! hard and fast rule!
# Now question might be clear if not let me explain we're given array of distance and speed of monsters,
# dist[i] means monster is at dist[i] km away from city and speed[i] means monster is moving at speed[i] km/minute,
# and we have to shoot those monster down with that fires 1 bullet per minute
# so we'll calulate time taken by monster to reach city, and sort in increasing order because we have to deal with monster 
# who are closer, then we'll start our gun firing at constant speed 1 bullet per minute, and we'll check if
# at specific time did monster already reahced city or not or at the time of firing they reached city(that is why we used equal sign also), 
# if reached means we lose and we'll return/print minute(number of monster) since we're firing at constant speed so minute fired = number of monster killed,