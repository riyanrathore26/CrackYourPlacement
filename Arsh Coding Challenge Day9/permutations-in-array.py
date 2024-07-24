
class Solution:
    def isPossible(self,a, b, n, k):
        trues = [False for _ in range(n)]
        a.sort(reverse=True)
        b.sort()
        for i in range(n):
            if a[i]+b[i] >= k:
                trues[i] = True
        if False in trues:
            return False
        else:
            return True
