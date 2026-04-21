class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        '''
        do union find and then sum how many unique parents
        '''

        parent = [i for i in range(N)]
        size = [1] * N

        def find(n):
            if n!=parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def merge(n, m):
            p1, p2 = find(n), find(m)
            if p1==p2:
                return False
            if size[p1]<=size[p2]:
                parent[p1] = p2
                size[p2] += size[p1]
            else:
                parent[p2] = p1
                size[p1] += size[p2]
            return True
        for n, m in edges:
            merge(n, m)
        res = set()
        for i in range(N):
            res.add(find(i))
        return len(res)