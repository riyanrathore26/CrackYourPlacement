
class NestedIterator:
    def __init__(self, nestedList):
        # Flatten the nested list during initialization
        self.flattened = self.flatten(nestedList)
        self.index = 0
    
    def flatten(self, nestedList):
        result = []
        for ni in nestedList:
            if ni.isInteger():
                result.append(ni.getInteger())
            else:
                result.extend(self.flatten(ni.getList()))
        return result

    def next(self):
        # Return the next element in the flattened list
        result = self.flattened[self.index]
        self.index += 1
        return result

    def hasNext(self):
        # Check if there are more elements to iterate
        return self.index < len(self.flattened)
