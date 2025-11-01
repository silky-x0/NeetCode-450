def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = head, head.next
    nums = set(nums)
    while head and head.val in nums:
        head = head.next

    while curr:
        if curr.val in nums:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head

