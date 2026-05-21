class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        root = TrieNode()
        for word in words:
            root.add(word)
        visit = set()

        def dfs(i, j, root, word):
            if (
                i < 0 or
                j < 0 or
                i >= ROWS or
                j >= COLS or
                (i, j) in visit or
                board[i][j] not in root.children
            ):
                return False
            letter = board[i][j]
            root = root.children[letter]
            word += letter
            if root.is_word: res.add(word)
            visit.add((i,j))
            for dr, dc in dirs:
                dfs(i+dr, j+dc, root, word)
            visit.remove((i,j))
            return


        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        return list(res)
