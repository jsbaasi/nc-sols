class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        union find, we go through each edge, and make a tree. all
        nodes should have the same parent
        """
        parents = [i for i in range(n)]
        size = [1] * n

        def find(node):
            if parents[node]!=node:
                parent = find(parents[node])
                parents[node] = parent
            return parents[node]

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2: return False
            if size[p1] >= size[p2]:
                parents[b] = p1
                size[p1] += size[p2]
            else:
                parents[a] = p2
                size[p2] += size[p1]
            return True
        
        for a,b in edges:
            if not union(a,b): return False
        
        for i in range(n-1):
            if find(i)!=find(i+1): return False
        return True
