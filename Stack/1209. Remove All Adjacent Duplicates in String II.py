# You are given a string s and an integer k, a k duplicate removal consists # of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. # It is guaranteed that the answer is unique.

 

# Example 1:
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

s = "deeedbbcccbdaa"

def removeDuplicates(self, s: str, k: int) -> str:
    stack = []  # each element: (char, count)

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1] = (c, stack[-1][1] + 1)
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append((c, 1))

    return "".join(ch * cnt for ch, cnt in stack)

print(removeDuplicates(s))

# Notes and Explanation (to be added)



# Key points:-
# count freq of character and push into stack with it
# if stack[-1] count reaches k pop that