"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.nmap = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        copy = Node(head.val)
        self.nmap[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.nmap[head.random] if head.random else None
        
        return copy