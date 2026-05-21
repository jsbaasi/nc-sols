class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            if w not in curr.children: return False
            curr = curr.children[w]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for w in prefix:
            if w not in curr.children: return False
            curr = curr.children[w]
        return curr.children is not None