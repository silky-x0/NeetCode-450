# Time Complexity: O(n^2)
# Space Complexity: O(1)

arr = [3,10,1,9,6,2,11]

for j in range(1,len(arr)):
    i = j-1
    key = arr[j]

    while i>=0 and arr[i] > key:
        arr[i+1] = arr[i]
        i-=1
    arr[i+1] = key

print(arr)        