import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.vals = []  # A list to store the values
        self.indices = defaultdict(set) 
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.indices[val].add(len(self.vals) - 1)
        return len(self.indices[val]) == 1 
    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        remove_index = self.indices[val].pop()
        last_val = self.vals[-1]
        self.vals[remove_index] = last_val
        self.indices[last_val].add(remove_index)
        self.indices[last_val].discard(len(self.vals) - 1)
        self.vals.pop()  # Remove the last element
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
