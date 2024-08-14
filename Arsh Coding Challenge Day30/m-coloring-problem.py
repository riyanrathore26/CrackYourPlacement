from collections import deque
def graphColoring(adj, k, V):
    color = [-1] * V

    def isSafe(node, c):
        for i in range(V):
            if graph[node][i] == 1 and color[i] == c: # type: ignore
                return False
        return True

    def solve(node):
        if node == V:
            return True
            
        for c in range(m): # type: ignore
            if isSafe(node, c):
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = -1
        return False

    return solve(0)
