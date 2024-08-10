import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashTable = collections.Counter(s)
        maxHeap = []
        for char, freq in hashTable.items():
            heapq.heappush(maxHeap, (-freq, char))

        prev_freq, prev_char = 0, ''
        result = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            result.append(char)
            if prev_freq < 0:
                heapq.heappush(maxHeap, (prev_freq, prev_char))
            prev_freq, prev_char = freq + 1, char
        result_str = ''.join(result)
        if len(result_str) != len(s):
            return ""
        return result_str