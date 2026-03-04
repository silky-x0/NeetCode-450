# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

root,tSum = [5,4,8,11,null,13,4,7,2,null,null,null,1], 22

def hasPathSum(root, tSum):
    if not root:
        return False

    rem = tSum - root.val
    if not root.left and not root.right:
        return rem == 0

    return hasPathSum(root.left, rem) or hasPathSum(root.right, rem)        