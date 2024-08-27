#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        left = [-1] * n
        right = [n] * n

        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = [0] * (n + 1)
        
        for i in range(n):
        # Length of the window in which arr[i] is the minimum
            length = right[i] - left[i] - 1
        # Update the answer for this window length
            ans[length] = max(ans[length], arr[i])

    # Some entries in ans[] may not be filled yet. Fill them by taking values from right side of ans[]
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])

    # Return the output array except the first entry (ans[0] is not used)
        return ans[1:]
