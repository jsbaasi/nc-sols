# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(l1, l2):
            if not l2: return l1
            l1 = rec(l1, l2.next)
            if l1.next == None: return l1
            if l1.next==l2: l2.next = None; return l2
            elif l1==l2: l1.next = None; return l1
            else:
                tmp = l1.next
                l1.next = l2
                l2.next = tmp
                return tmp
        
        head = rec(head, head.next)