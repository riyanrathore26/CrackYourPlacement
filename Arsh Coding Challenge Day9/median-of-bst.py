def findMedian(root):
    result = []
    def dfs(root, result):
        if root is None:
            return
        dfs(root.left, result)
        result.append(root.data)
        dfs(root.right, result)
    dfs(root, result)
    n = len(result)
    if n % 2 == 0:
        median = n // 2
        temp = (result[median - 1] + result[median]) / 2.0
        if temp.is_integer():
            return int(temp)
        else:
            return temp
    else:
        median = n // 2
        return result[median]
