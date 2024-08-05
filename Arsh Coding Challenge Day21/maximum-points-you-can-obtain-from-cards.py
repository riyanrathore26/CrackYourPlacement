from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        total = sum(cardPoints[:k])
        max_score = total
        for i in range(1, k + 1):
            total = total - cardPoints[k - i] + cardPoints[-i] #every time i removing one element from left and adding one elelment from right and so on this is reason that i am making mistake that i am picking up all element from middle
            max_score = max(max_score, total)
        return max_score