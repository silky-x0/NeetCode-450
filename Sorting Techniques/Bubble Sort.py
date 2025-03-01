# Time Complexity: O(n^2)
# Space Complexity: O(1)

arr = [2, 10, 51, 9, 5, 0, 3, 1]

def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        if not swapped:
            break        

    return arr

print(bubbleSort(arr))          

# Flag helps to maintain efficiency, say if already sorted array is given we have to check at least n times    Best Case = O(n) (w/out flag)
# Obviously we have to traverse over array at least one time but with flag variable we can skip that part.     Best Case = (1)  (w/ flag)

