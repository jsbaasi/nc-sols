class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        we need to find the cycle
        '''
        N = len(edges)
        parent = [i for i in range(N+1)]
        height = [1] * (N+1)

        def find(n):
            if n!=parent[n]:
                return find(parent[n])
            return n
        
        def union(n, m):
            p, q = find(n), find(m)
            if p==q:
                return False
            if height[p]<=height[q]:
                parent[p] = q
                height[q] += height[p]
            else:
                parent[q] = p
                height[p] += height[q]
            return True
        
        for n, m in edges:
            if not union(n,m):
                return [n,m]




        

        