# You are given an array people where people[i] is the weight of the ith person, and an infinite number 
# of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, 
# provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.


# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

people = [3,5,3,4]
limit = 5

l, r = 0, len(people) - 1
b = 0  # Number of boat

while l <= r:
    b += 1
    if people[l] + people[r] <= limit:
        l += 1
        r -= 1
    else:
         r -= 1


print(b)             


# Notes and Explanation
# First of all question boat can two people at time and me dumbarse was thinking many people within limit
# I wasted my 25 min, F!, Umm so question we'll have to assign boats or choose minimum number boats such as every person can
# be saved. 

# Approach
# We'll start by sorting first, why? because we wanna get this done with minimum number of boats as possible
# So we'll be greedy and sort the array, By sorting we can pair the lightest and heaviest person together if possible
# So we'll use two pointer approach, one pointer at start and one at end
# We'll check if the sum of both pointer is less than or equal to limit, if yes
# then we can save both people in one boat, so we'll move both pointers inward
# If not then we'll move only right pointer inward because the heaviest person cannot be paired with anyone
# [So we'll move only right pointer inward and assign a boat to that person]
# We'll keep increasing boat count in each iteration because at least one person will be saved in each boat
# We'll continue this until both pointers meet or cross each other