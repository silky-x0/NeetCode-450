# this problem is same as house robber except last and 1 house are connected .ie in circle
# I figured it out that we have to run two loops for different choice coz of constraints

nums = [1,2,3,1]
def maxRob2(nums:list) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]                   #there was a test case nums = [1] and befire i didnt put this condn
    rob1,rob2 = 0, 0
    for i in range(n-1):
        newRob = max(rob1+nums[i],rob2)
        rob1 = rob2
        rob2 = newRob

    rob3,rob4 = 0, 0
    for i in range(1,n):
        newRob = max(rob3+nums[i],rob4)
        rob3 = rob4
        rob4 = newRob

    return max(rob2,rob4)    
                

print(maxRob2(nums))                