import math

class Solution:
    def findDeterminant(self, Matrix):
        # Variable to store the determinant value
        det = 0
        if len(Matrix) == 1:
            return Matrix[0][0]

        elif len(Matrix) == 2:
            det = (Matrix[0][0] * Matrix[1][1] - Matrix[0][1] * Matrix[1][0])
            return det

        else:
            for p in range(len(Matrix[0])):
                tempMatrix = []
                for i in range(1, len(Matrix)):
                    row = []
                    for j in range(len(Matrix[i])):
                        if j != p:
                            row.append(Matrix[i][j])

                    if len(row) > 0:
                        tempMatrix.append(row)

                det = det + Matrix[0][p] * (-1) ** p * self.findDeterminant(tempMatrix)

            return det

    def countSpanningTrees(self, graph, n, m):
        adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(graph)):
            x = graph[i][0]
            y = graph[i][1]
            adjMatrix[x][y] = 1
            adjMatrix[y][x] = 1
        degree = [0] * n

        for i in range(n):
            for j in range(n):
                if adjMatrix[i][j] == 1:
                    # Calculating degree of each node
                    degree[i] += 1
        # Updating the values of primary diagonal with degree of the node
        for i in range(n):
            adjMatrix[i][i] = degree[i]

        # Replacing all 1 in the matrix which are not present on primary diagonal with -1
        for i in range(n):
            for j in range(n):
                if i != j and adjMatrix[i][j] == 1:
                    adjMatrix[i][j] = -1

        # Submatrix of size (n-1)*(n-1) in which 1st row and 1st column values will not be there
        submatrix = [[0 for _ in range(n - 1)] for _ in range(n - 1)]

        for i in range(1, n):
            for j in range(1, n):
                submatrix[i - 1][j - 1] = adjMatrix[i][j]

        # This will be the answer as (-1)^(1+1) will be equal to 1 only
        return self.findDeterminant(submatrix)

