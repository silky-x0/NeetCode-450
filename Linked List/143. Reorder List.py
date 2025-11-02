# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]



def reorderList(head):

    # Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev, curr = None, slow

    while curr:
        nxt_node = curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node

    # Merge the two halves
    first, second = head, prev
    while second.next:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


# Notes:
# - The solution first finds the middle of the linked list using the slow and fast pointer technique.
# - It then reverses the second half of the list.
# - Finally, it merges the two halves by alternating nodes from each half.
# - The time complexity is O(n) and the space complexity is O(1).            
