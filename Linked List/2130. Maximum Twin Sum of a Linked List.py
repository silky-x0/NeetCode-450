# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, 
# if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.


# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 


def pairSum(head):
    if not head.next:
        return head.val  # As question guarentees as least one element

    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow
    while curr:
        nxt_node = curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node

    first, second, max_ = head, prev, -1
    while second:
        max_ = max(first.val + second.val, max_)
        first = first.next
        second = second.next

    return max_

# Notes:
# Question simply says, there is linked of even length, and each node is paired with node n-1-i or n-1-i apart.
# so we just have to return the max sum of two nodes among all pairs
# this question is same as LC 143, which I did a moment earlier so was easy to grasp what to do.

# Approach:
# - We'll find half and linked List first
# - Then we'll reverse half of linked list coz we have to add simultaneously first and 2nd half to find max twin sum
# - if it were doubly linked list we dont need to reverse it but anyways
# after reversing we'll traverse in first and second half simultaneously and keep adding value of both node to keep track max sum.