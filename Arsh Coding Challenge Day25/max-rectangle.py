#User function Template for python3


class Solution:
    def maxArea(self,matrix, n, m):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0] * n  
        right = [n] * n 
        height = [0] * n

        max_area = 0

        for i in range(m):
            cur_left, cur_right = 0, n

            for j in range(n):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

        # Update left boundary array
            for j in range(n):
                if matrix[i][j] == 1:
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

        # Update right boundary array
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 1:
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j

        # Calculate maximum area for each cell
            for j in range(n):
                max_area = max(max_area, (right[j] - left[j]) * height[j])

        return max_area
