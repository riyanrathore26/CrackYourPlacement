#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        result = []
        
        def backTrack(start, path):
            if start == len(S):
                result.append(path[:])
            for i in range(start, len(S)):
                current_str = S[start:i+1]
                if current_str == current_str[::-1]:
                    backTrack(i + 1, path + [current_str])
        backTrack(0, [])
        return result
obj = Solution()
re = obj.allPalindromicPerms("aab")
print(re)