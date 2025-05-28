arr = [4,1,-1,2,-1,2,3]
k = 2
#op - [1,2]

map = {}
for num in arr:
    if num in map:
        map[num]+=1
    else:
        map[num]=1    

tempArr = sorted(map.items(),key=lambda x: x[1], reverse=True)
arrAns = []
for i in range(k):
    arrAns.append(tempArr[i][0])

print(arrAns)


#Time Complexity O(nlogn) naive approach LC said to do better than this but whatever.
#Got Method that uses Heap sort and other that uses bucket sort
#those I'll be implementing it later