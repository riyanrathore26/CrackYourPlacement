class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        left = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
        return len(s) - left