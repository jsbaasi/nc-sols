class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj_list = defaultdict(list)
        letters = set()
        for i in range(n-1):
            w1, w2 = words[i], words[i+1] if i+1<n else ""
            n1, n2 = len(w1), len(w2)
            if n2<n1 and w1[:n2]==w2[:n2]: return ""
            letters.update(w1+w2)
            for j in range(min(n1,n2)):
                if w1[j]!=w2[j]: adj_list[w1[j]].append(w2[j]); break
        
        visit = set()
        res = []
        print(adj_list)
        def dfs(node):
            if node in visit: return False
            if node in res: return True

            visit.add(node)
            for edge in adj_list[node]:
                if not dfs(edge): return False
            adj_list[node].clear()
            visit.remove(node)
            res.append(node)

            return True
        for c in (words[i][j] for i in range(n) for j in range(len(words[i]))):
            if not dfs(c): return "" 
        return "".join(res[::-1])