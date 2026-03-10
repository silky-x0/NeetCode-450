# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22



def pathSum(root, tsum):
    if not root:
        return []
    res = []
    
    def trav(node, path, cSum):
        path.append(node.val)
        cSum += node.val

        leaf = not node.left and not node.right
        if leaf and tsum == cSum:
            res.append(path[:])

        if node.left:
            trav(node.left, path, cSum)

        if node.right:
            trav(node.right, path, cSum)

        return

    trav(root, [], 0)
    return res

# If you solved path sum 1, this is simple requires dfs only.
# Also we can track remaining sum instead of current sum(cSum) 
# to avoid using this (tSum == cSum) at every leaf.    