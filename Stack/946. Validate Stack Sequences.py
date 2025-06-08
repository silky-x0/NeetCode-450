# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

def validStackSeq(pushed:list[int], popped:list[int])-> bool:
    stack = []
    j = 0       # To track popped element
    for elem in pushed:
        stack.append(elem)
        while stack and j < len(pushed) and stack[-1] == popped[j]:
            stack.pop()
            j+=1
    return not stack

print(validStackSeq([1,2,3,4,5], [4,5,3,2,1]))

# Bro literally I was so close to the solution only mistake I made that I didnt check if
# stack was empty and j is less than length of pushed, so for this part I wasted my
# 30 minutes, and main logic I did in 6-10 minutes.

# Time Complexity: O(n) where n is the length of pushed or popped
# Space Complexity: O(n) for the stack