"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        orig = head
        orig_to_copy = defaultdict(lambda: Node(0))
        while orig:
            copy = orig_to_copy[orig]
            copy.val = orig.val
            if not orig.next:
                copy.next = None
            else:
                copy.next = orig_to_copy[orig.next]
            if not orig.random:
                copy.random = None
            else:
                copy.random = orig_to_copy[orig.random]
            orig = orig.next
        return orig_to_copy[head] if head else None