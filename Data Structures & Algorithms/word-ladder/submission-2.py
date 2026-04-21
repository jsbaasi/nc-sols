class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjacency_list = defaultdict(list)
        n = len(wordList[0])
        for word in wordList:
            for i in range(n):
                adjacency_list[word[0:i] + "*" + word[i+1:n]].append(word)
        
        visit=set()
        print(adjacency_list)
        def bfs(q):
            res = 0
            while q:
                for _ in range(len(q)):
                    word = q.popleft()
                    if word==endWord:
                        return res
                    for i in range(n):
                        for next_word in adjacency_list[word[0:i] + "*" + word[i+1:n]]:
                            if next_word not in visit:
                                visit.add(next_word)
                                q.append(next_word)
                res+=1
            return -1

        visit.add(beginWord)
        rc = bfs(deque([beginWord]))
        return rc+1 if rc!=-1 else 0