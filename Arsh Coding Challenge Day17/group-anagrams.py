from collections import Counter,defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = Counter(s)
            key = tuple(sorted(count.items()))
            anagrams[key].append(s)
        
        return list(anagrams.values())    