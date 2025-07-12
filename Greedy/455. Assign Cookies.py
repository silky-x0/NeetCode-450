# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and 
# each cookie j has a size s[j]. If s[j] >= g[i],we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

child = [1,2,3]  #g
cookie = [1,1]   #s

child.sort()
cookie.sort()
i, j = 0, 0
while i < len(child) and j < len(cookie):                             # for larger inputs store length of both in variable to avoid overhead calls!
    if cookie[j] >= child[j]:
        i+=1
    j+=1

print(i)

# Notes and Explanation
# Idea is straight forward first sort both cokkies and childs, you ask why? because it'll be easier to compare say if we didn't sort we have to find 
# cookie that is larger and equal to the child's greed and when assigned we have to remove that cookie from array then again find and while doing all
# this we have to try multiple combination like what is we assigned largest cookies to few children which can be later used for example
# child = [2,1,3] cookie = [4,3,2] say we assigned cookie[0] to child[0] then cookie[1] to child[1] now we cant assigned last cookie to our child[2] coz it has
# greed of 3 i.e greater then cookie's value but in question it says cookie should be larger or equal to child's greed, and you can diffrent combination for 
# max number of children satisfied(with cookie), but use can use sorting beforehand to this mess. Now you understand why we did this right!!
# moving onto next part we also have to check if either cookie or number of children has reached its max length to avoid index error
# now we can simply start while loop with these condition and inside we'll check our main condtion if cookie is larger or equal to child's greed
# if yes we can move our i pointer by one indicating one child is satisfied(with cookie) and we also have to increase our j pointer coz we cannot assign same
# cookie to other or if current cookie isn't greater or equal to current child's greed so simple we'll keep increasing j and increase i when conditions are met 