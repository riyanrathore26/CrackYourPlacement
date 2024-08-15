class Solution:
    def missingNumber(self, arr, n):
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr = arr[j:]
        n = len(arr)

        # Step 3: Use the index of the array as a hash to mark the presence of elements
        for i in range(n):
            val = abs(arr[i])
            if val - 1 < n and arr[val - 1] > 0:
                arr[val - 1] = -arr[val - 1]
        for i in range(n):
            if arr[i] > 0:
                return i + 1
        return n + 1