from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def merge_sort(start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            left, right = nums[start:mid + 1], nums[mid + 1:end + 1]
            l = r = 0
            for k in range(start, end + 1):
                if l < len(left) and (r >= len(right) or left[l] <= right[r]):
                    nums[k] = left[l]
                    l += 1
                else:
                    nums[k] = right[r]
                    r += 1
            
            return count
        
        return merge_sort(0, len(nums) - 1)
