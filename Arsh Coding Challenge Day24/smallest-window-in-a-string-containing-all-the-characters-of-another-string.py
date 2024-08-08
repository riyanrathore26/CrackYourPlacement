#User function Template for python3
from collections import defaultdict

class Solution:
    def smallestWindow(self, s, p):
        if not s or not p:
            return ""
        
        hashTable = defaultdict(int)
        for char in p:
            hashTable[char] += 1
        
        required = len(hashTable)
        formed = 0
        window_counts = defaultdict(int)
        
        l, r = 0, 0
        min_len = float('inf')
        min_window = ""
        
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            
            if char in hashTable and window_counts[char] == hashTable[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                
                window_counts[char] -= 1
                if char in hashTable and window_counts[char] < hashTable[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return min_window if min_len != float('inf') else "-1"
