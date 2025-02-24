# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

ops = ["5","2","C","D","+"]

stack = []
for op in ops:
    if op == "+":
        stack.append(stack[-1]+ stack[-2])
    elif op == "D":
        stack.append(stack[-1]*2)
    elif op == "C":
        stack.pop()
    else:
        stack.append(int(op))

print(sum(stack))  #return sum(stack)

# Time complexity: O(n)
# Space complexity: O(n)
     