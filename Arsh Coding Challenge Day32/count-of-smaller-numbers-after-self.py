from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(indices):
            half = len(indices) // 2
            if half:
                left, right = merge_sort(indices[:half]), merge_sort(indices[half:])
                for i in range(len(indices) - 1, -1, -1):
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        smaller[left[-1]] += len(right)
                        indices[i] = left.pop()
                    else:
                        indices[i] = right.pop()
            return indices

        smaller = [0] * len(nums)
        merge_sort(list(range(len(nums))))
        return smaller