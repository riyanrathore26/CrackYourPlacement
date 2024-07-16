class Solution:

    def findMinDiff(self, A,N,M):
        if len(A) < M:
            return 
        A.sort()
        diffrence = float('inf')
        i,j = 0,M-1
        while j != len(A):
            diffrence = min(diffrence,A[j]-A[i])
            i+=1
            j+=1
        
        return diffrence