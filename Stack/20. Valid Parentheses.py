# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

s = "()[}"
stack = []
closeToOpen = {")":"(","}":"{","]":"["}

for str in s:
    if str in closeToOpen:
        if stack and stack[-1] == closeToOpen[str]:
            stack.pop()
        else:
            print("False")  # return False
    else:
        stack.append(str)
      

print(0 == len(stack))            # or return not stack!!


# Time complexity: O(n)  //we used hashTable for efficient lookup i.e in constant time.
# Space complexity: O(n) //we created stack for n elements and dict for n, which add upto O(2n) which simplifies to O(n).
# Although Constant matter in real time projects but not here!