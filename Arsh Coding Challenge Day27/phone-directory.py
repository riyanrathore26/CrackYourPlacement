class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_all_words_with_prefix(self, prefix):
        results = []
        node = self.search_prefix(prefix)
        if node is None:
            return results
        
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results)

    def displayContacts(self, n, contact, s):
        # Insert all contacts into the Trie
        for name in contact:
            self.insert(name)

        # Search for each prefix of the query string `s`
        prefix = ""
        output = []
        for char in s:
            prefix += char
            matching_contacts = self.get_all_words_with_prefix(prefix)
            if matching_contacts:
                output.append(sorted(matching_contacts))
            else:
                output.append(["0"])

        return output
