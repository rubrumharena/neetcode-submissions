# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        cur = head
        rev_head = ListNode(val=head.val)
        while cur.next:
            rev_head = ListNode(val=cur.next.val, next=rev_head)
            cur = cur.next
        return rev_head
