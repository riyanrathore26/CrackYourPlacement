from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            length = len(strs[0])
            i = 0
            result = ""
            while i < length:
                for word in strs:
                    if i >= len(word) or word[i] != strs[0][i]:
                        return result
                result += strs[0][i]
                i += 1

            return result