# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast: break
        return True if slow==fast else False