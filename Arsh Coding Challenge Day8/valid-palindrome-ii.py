class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # Try removing one character from either side
                temp1 = s[:i] + s[i + 1:]  # Remove character at i
                temp2 = s[:j] + s[j + 1:]  # Remove character at j
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]

        return True