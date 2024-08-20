from typing import List

class Solution:
    def minDifference(self, n: int, arr: List[int]) -> List[List[int]]:
        total_sum = sum(arr)
        min_diff = float('inf')
        best_partition = ([], [])

        def tugOfWarUtil(i, current_sum, selected_count, selected):
            nonlocal min_diff, best_partition

            if selected_count == n // 2:
                subset1 = [arr[j] for j in range(n) if selected[j]]
                subset2 = [arr[j] for j in range(n) if not selected[j]]
                current_diff = abs((total_sum - current_sum) - current_sum)
                if current_diff < min_diff:
                    min_diff = current_diff
                    best_partition = (subset1, subset2)
                return

            if i >= n:
                return

            # Include the current element in the first subset
            selected[i] = True
            tugOfWarUtil(i + 1, current_sum + arr[i], selected_count + 1, selected)

            # Exclude the current element from the first subset
            selected[i] = False
            tugOfWarUtil(i + 1, current_sum, selected_count, selected)

        # Initialize the selected array
        selected = [False] * n
        
        # Start the recursion
        tugOfWarUtil(0, 0, 0, selected)
        
        return best_partition
