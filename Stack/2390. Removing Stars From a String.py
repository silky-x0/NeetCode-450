# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

def removeAccStar(s:str):
    stack = []
    for char in s:                #O(n)
        if char == "*":
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

print(removeAccStar("leet**cod*e"))

#What i originally going to do was make two stack for separate star and letters then
#run while loop until star is empty simultanously but it was wrong obviously then suddenly
#I remembered in 3rd sem we were taught solving expression using stack so i applied that here
