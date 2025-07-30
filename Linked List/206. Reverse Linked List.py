# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def addEnd(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        return

    def display(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        print(res)
        return
    
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            # temp = curr.next
            # curr.next = prev
            # prev = curr
            # curr = temp

            curr.next, prev, curr = prev, curr, curr.next

        self.head = prev   
    

ll = linkedList()                
ll.addEnd(1)                
ll.addEnd(2)                
ll.addEnd(3)
ll.addEnd(4)
ll.addEnd(5)
print(f"before reversing{ll.display()}")
ll.reverse()
print(f"After reversing {ll.display()}")
