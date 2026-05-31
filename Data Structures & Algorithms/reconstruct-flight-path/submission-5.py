from itertools import permutations
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        how do we track all edges used?
        '''
        tickets.sort(key=lambda x:x[1])
        adj_list = defaultdict(list)
        for i, (start, end) in enumerate(tickets):
            adj_list[start].append(i)
        res = []
        trav = set()
        def dfs(node):
            if len(trav)==len(tickets): return True
            elif all((i in trav for i in adj_list[node])): return False
            unused = list(filter(lambda i: i not in trav, adj_list[node]))
            for p in permutations(unused):
                for i,v in enumerate(p):
                    if v in trav: continue
                    trav.add(v)
                    res.append(tickets[v][1])
                    if dfs(tickets[v][1]): return True
                    for j in range(i, -1, -1):
                        if p[j] not in trav: continue
                        trav.remove(p[j])
                        res.pop()
            return False
        dfs("JFK")
        return ["JFK"] + res