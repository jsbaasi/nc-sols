# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        def merge_two_lists_rec(l1,l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val<=l2.val:
                l1.next = merge_two_lists(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_lists(l1, l2.next)
                return l2
        
        def merge_two_lists(l1,l2):
            tail = dummy = ListNode()
            while l1 or l2:
                if not l1:
                    tail.next = l2
                    l2 = None
                elif not l2:
                    tail.next = l1
                    l1 = None
                elif l1.val<=l2.val:
                    tail.next, l1 = l1, l1.next
                    tail = tail.next
                else:
                    tail.next, l2 = l2, l2.next
                    tail = tail.next
            return dummy.next

        while len(lists)>1:
            n = len(lists)
            tmp_lists = []
            for i in range(0, n, 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<n else None
                tmp_lists.append(merge_two_lists(l1,l2))
            lists = tmp_lists
        return lists[0]