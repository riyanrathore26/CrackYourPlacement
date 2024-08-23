from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        graph = defaultdict(set)
        in_degree = {chr(i + ord('a')): 0 for i in range(k)}

        for i in range(n - 1):
            first_word, second_word = dict[i], dict[i + 1]
            min_length = min(len(first_word), len(second_word))
            for j in range(min_length):
                if first_word[j] != second_word[j]:
                    if second_word[j] not in graph[first_word[j]]:
                        graph[first_word[j]].add(second_word[j])
                        in_degree[second_word[j]] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""

        queue = deque([char for char in in_degree if in_degree[char] == 0])
        alien_order = []

        while queue:
            char = queue.popleft()
            alien_order.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(alien_order) < len(in_degree):
            return ""

        return "".join(alien_order)