# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(head, prev, k, head_connection) -> Optional[ListNode]:
            new_tail = head
            for _ in range(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            head_connection.next = prev
            return new_tail
        '''
        edge cases how to get the head of reversed lists?
        '''
        dummy = ListNode(0, head)
        l = dummy; r = head
        while True:
            for _ in range(k):
                if not r: return dummy.next # break out of while loop
                r = r.next
            l = reverse_list(l.next, r, k, l)
            if not r: return dummy.next