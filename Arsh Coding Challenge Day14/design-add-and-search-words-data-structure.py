class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for chrs in word:
            if chrs not in node.children:
                node.children[chrs] = TrieNode()
            node = node.children[chrs]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, chrs in enumerate(word):
                if chrs == '.':
                    for child in node.children.values():
                        if search_in_node(word[i + 1:], child):
                            return True
                    return False
                else:
                    if chrs not in node.children:
                        return False
                    node = node.children[chrs]
            return node.is_end_of_word

        return search_in_node(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
