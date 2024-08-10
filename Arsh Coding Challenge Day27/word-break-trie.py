class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word, start, end):
        node = self.root
        for i in range(start, end):
            char = word[i]
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end_of_word:
                return True
        return False

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        trie = Trie()

        # Insert all words in wordDict into the Trie
        for word in wordDict:
            trie.insert(word)

        # DP array to keep track of break points
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # Check substrings
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and trie.search(s, j, i):
                    dp[i] = True
                    break

        return dp[len(s)]