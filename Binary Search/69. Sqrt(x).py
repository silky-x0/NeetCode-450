num = 4
i, j = 0, num
while i <= j:
    mid = (i + j) // 2
    if mid * mid == num:
        print(mid)
        break
    elif mid * mid < num:
        i = mid + 1
    else:
        j = mid - 1
else:
    print(j)
# Time Complexity: O(log n)
# # Space Complexity: O(1)       