# User function Template for python3

class Solution:
    def search(self, pattern, text):
        result = []
        n = len(text)
        m = len(pattern)
        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                result.append(i + 1)
        return result
