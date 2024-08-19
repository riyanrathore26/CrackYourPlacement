from typing import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        st = Counter(s)
        total = 0
        unique = set()
        for i,x in st.items():
            while x > 0 and x in unique:
                x-=1
                total+=1
            unique.add(x)
        return total