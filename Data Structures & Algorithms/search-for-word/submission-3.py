class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
    def add(self, word):
        curr = self
        for w in word:
            if w not in curr.children: curr.children[w] = Trie()
            curr = curr.children[w]
        curr.is_word = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visit = set()
        root = Trie()
        root.add(word)
        def dfs(i: int, j: int, w: str, root):
            if i<0 or j<0 or i>=ROWS or j>=COLS or (i,j) in visit: return False
            if board[i][j] not in root.children: return False
            w = w + board[i][j]
            root = root.children[board[i][j]]
            if root.is_word: return True
            visit.add((i,j))
            for dr, dc in dirs:
                if dfs(i+dr, j+dc, w, root): return True
            visit.remove((i,j))

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, "", root): return True
        return False