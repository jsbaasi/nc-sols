# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        2 4 6 8
        2 8 4 6

        2 4 6 8 10
        2 4 6 bias to first list
        10 8
        2 10 4 8 6
        '''
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            if not (fast and fast.next): prev = slow; slow = slow.next; prev.next = None
            else: slow = slow.next
        if slow==fast: return
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        head2 = prev
        tail = ListNode()
        while head:
            tail.next = head
            head = head.next
            tail = tail.next
            tail.next = head2
            if head2:
                head2 = head2.next
                tail = tail.next