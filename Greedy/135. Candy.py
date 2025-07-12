# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

ratings = [1,0,2]
n = len(ratings)
toffee = [1]*n

for i in range(1,n):
    if ratings[i] > ratings[i-1]:
        toffee[i] = toffee[i-1] + 1

for j in range(n-2,-1,-1):
    if ratings[j] > ratings[j+1]:
        toffee[j] = max(toffee[j], toffee[j+1] + 1)

print(sum(toffee))                                                       # Time and Space Complexity is O(n)

# Notes and Explanation 🥰

# So the idea is simple we have to give atleast one candy to each child, so we intialised toffee array with 1's
# now going left to right from index 1 to n-1 why? coz question said children are to be given more candies than its neighbour
# if current child rating is more than any one neighbour and we're greedy and stingy(kannjoos) so we'll give exactly one candy more
# now while traversing we'll check if current child rating is greater than previous child's if yes add one candy more to total candies of previous child(child to left) give to
# current child, keep in my we didn't checked on child on index 0, now traversing right to left, we;ll start from n-2 to 0, we'll check same condition but
# one extra check that what if current child aready has more candies than its neighbour and accidently give him less candies that'll nullify our 1st traversal check
# so we can compare if current child rating is greater than next child(child to right) rating and max value of candy current child has and next child's candy + 1
# I know above might me confusing like I explained but once you look at code it'll be clear.

# And previous I was doing assign cookies question[LC 455], greedy [easy].....I saw this question I was oke i can do it, to be honest while doing I already
# wrote greeedy approach but I was stuck as index error issue 😭😭 because I was simulatenously comparing  currrent child with its left and right neighbour 
# I know this is dumb right😭, and 2nd thought what came into my mind is lets traverse 1 to n-2 and check separately first and last element to avoid that index error 
# but this approach doesnt gurantee that constarint will be followed, so inevitably we'll have to do with two pass.