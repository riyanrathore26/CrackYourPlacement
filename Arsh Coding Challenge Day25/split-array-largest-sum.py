from typing import List


def is_possible(arr, n, m, max_pages):
    student_count = 1
    current_pages = 0
    
    for i in range(n):
        if current_pages + arr[i] > max_pages:
            student_count += 1
            current_pages = arr[i]
            
            if student_count > m:
                return False
        else:
            current_pages += arr[i]
    
    return True
class Solution:
    def splitArray(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m > n:
            return -1  
        low = max(arr)
        high = sum(arr)
        result = high
    
        while low <= high:
            mid = (low + high) // 2
        
            if is_possible(arr, n, m, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return result
