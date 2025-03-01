
arr = [2,10,51,9,5,0,3,1]

def SelectionSort(arr):
    for i in range(len(arr)-1):
        minElem = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[minElem]:
                minElem = j 

        arr[minElem], arr[i] = arr[i], arr[minElem]          

    return arr

print(SelectionSort(arr))                