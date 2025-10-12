class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]

        curr.terminal = True  # mark the end of the word

    def search(self, word: str) -> bool:

        def dfs(j, curr):
            for i in range(j, len(word)):
                ch = word[i]

                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]

            return curr.terminal

        return dfs(0, self.root)
