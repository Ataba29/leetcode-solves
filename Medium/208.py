class Trie:

    def __init__(self):
        self.Childern = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for i in range(len(word)):
            idx = ord(word[i]) - ord("a")
            if node.Childern[idx] == None:
                node.Childern[idx] = Trie()
            node = node.Childern[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.Childern[idx] == None:
                return False
            node = node.Childern[idx]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if node.Childern[idx] == None:
                return False
            node = node.Childern[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
