class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children: curr.children[w]=TrieNode()
            curr = curr.children[w]
        curr.is_word = True

    def rec(self, root, word) -> bool:
        if not word: return root.is_word
        else:
            w = word[0]
            if w==".":
                for letter, node in root.children.items():
                    if self.rec(node, word[1:]): return True
                return False
            else:
                return False if w not in root.children else self.rec(root.children[w], word[1:])

    def search(self, word: str) -> bool:
        return self.rec(self.root, word)