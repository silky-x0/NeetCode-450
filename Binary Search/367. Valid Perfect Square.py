#Check if a number is a valid perfect square using binary search
num = 16
i , j = 1, num
while i <= j:
    mid = (i + j)//2
    if mid*mid == num:
        print("Valid Square")
        break
    elif mid*mid < num:
        i = mid + 1
    else:
        j = mid - 1
else:
    print("Not valid square")

# Time Complexity: O(log n)
# Space Complexity: O(1)                   