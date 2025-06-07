# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

#Well to be very honest I was confused at the question what i had in mind that i would find greatest element
#then add 1 to each element until it euquals to that greatest element while counting
#how many times i have added one, already build up logic but in the discussion section
# i've found alternate way, let me show you that

def minimumMovesReq(nums):
    if not nums or len(nums) == 1:   #Edge case
        return 0
    minVal = min(nums)
    totalMoves = 0
    for num in nums:
        totalMoves+=(num-minVal)

    return totalMoves

# So instead of increasing element we'll decrease it until all becomes the same
# and adding them to totalmoves and totalmovrs needed to decrease will be
# current element minus minimum element in our case
# now I think what i thought works fine but this works better

