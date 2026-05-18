class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        new_head = None
        def dfs(curr):
            if curr.next == None:
                nonlocal new_head
                new_head = curr
                return curr
            dfs(curr.next).next=curr
            return curr
        dfs(head)
        head.next = None
        return new_head