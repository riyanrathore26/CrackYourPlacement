class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                elif matrix[i][j] != -1:
                    dist[i][j] = matrix[i][j]
        # Apply Floyd Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        # # Update the input matrix with shortest distances
        for i in range(n):
            for j in range(n):
                if dist[i][j] == float('inf'):
                    matrix[i][j] = -1
                else:
                    matrix[i][j] = dist[i][j]