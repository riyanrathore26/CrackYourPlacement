import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(pair[0]**2 + pair[1]**2), pair) for pair in points]
        distances.sort(key=lambda x: x[0])
        closest_points = [pair for _, pair in distances[:k]]
        return closest_points