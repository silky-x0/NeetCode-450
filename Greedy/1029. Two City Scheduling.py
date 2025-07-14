# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
# the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

# Example 1:
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

costs = [[10,20],[30,200],[400,50],[30,20]]
costs.sort(key = lambda x: x[0] - x[1])

n = len(costs)//2
total = 0

for i in range(n):
    total+=costs[i][0]

for i in range(n,2*n):
    total+=costs[i][1]

print(total)


# Notes and Explanation

# According to the question we have to send equal number of people to each city and minimize cost
# Our main idea is to find difference between city A and B, and sort it
# If diff < 0 → City A is cheaper → we "save" money by sending them to A
# If diff > 0 → City B is cheaper → we "save" money by sending them to B
# If diff == 0 → Same cost either way → doesn’t matter
# since we've to send equal number of people we'll divide half and send to city A
# and rest half to city B.


# Alternative Approach(this is intuitive for me)🥰🥰

# We'll first send everyone to city A and find refund or cost to change city from A to B i.e difference between each city
# then we'll sort the cost, you may ask why? because we need to send half people to city B and minimize the cost so we'll pick
# top city which has less exchange cost

costs = [[10,20],[30,200],[400,50],[30,20]]
total1 = 0

for cost in costs:
    total1+=cost[0]                                     # sending everyone to city A

costA_B = []
for cost in costs:
    costA_B.append(cost[1] - cost[0])                  # cost of switching from A to B....(B-A)
    
costA_B.sort()
n = len(costs)//2                                      

for i in range(n):                                     # sending people with less switching cost to B, we're adding because
    total1+=costA_B[i]                                 # if we if city B is cheaper it'll minimize the cost if it'll increase
                                                       # but still we have to send half to city B
print(total1)

