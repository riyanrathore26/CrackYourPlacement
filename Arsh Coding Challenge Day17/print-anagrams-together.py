#User function Template for python3
from collections import Counter,defaultdict

class Solution:
    def Anagrams(self, words, n):
        anagrams = defaultdict(list)
        for s in words:
            count = Counter(s)
            key = tuple(sorted(count.items()))
            anagrams[key].append(s)
        
        return list(anagrams.values())    
