nums = [1,2,0,1,2,0,0,1,0]

#Original approach 3 pointers(Dutch flag algo)
i,j,k = 0,0,len(nums)-1
while j <= k:
    if nums[j] == 0:
        nums[j],nums[i] = nums[i],nums[j]
        i+=1
        j+=1
    elif nums[j] == 1:
        j+=1
    else:
        nums[j],nums[k] = nums[k],nums[j]
        k-=1
print(*nums)

#Alternate approach counting values of each 0, 1 and 2 the filling array
zero, one, two = nums.count(0), nums.count(1), nums.count(2)
for i in range(zero):
    nums[i] = 0
for i in range(zero,zero+one):
    nums[i] = 1
for i in range(zero+one,zero+one+two):
    nums[i] = 2

print(*nums)            