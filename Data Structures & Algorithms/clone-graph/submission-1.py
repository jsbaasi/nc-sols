"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {} # old node mapping to it's copy

        def dfs(node): # returns a deep copy of a node
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = Node(node.val)
            for n in node.neighbors:
                old_to_new[node].neighbors.append(dfs(n))
            
            return old_to_new[node]
        
        if not node:
            return None
        elif not node.neighbors:
            return Node(1)
        else:
            return dfs(node)
