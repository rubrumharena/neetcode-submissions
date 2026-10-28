class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        rev = None
        n = 0
        cur = head
        while cur:
            rev = ListNode(cur.val, rev)
            n += 1
            cur = cur.next

        dummy = ListNode()
        tail = dummy
        for i in range(n):
            if i % 2 == 0:
                tail.next = head
                head = head.next 
            else:
                tail.next = rev
                rev = rev.next  
            tail = tail.next

        tail.next = None        