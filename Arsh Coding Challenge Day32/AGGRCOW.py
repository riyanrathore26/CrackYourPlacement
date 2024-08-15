def canPlaceCows(stalls, n, cows, min_dist):
    count = 1  # place the first cow in the first stall
    last_position = stalls[0]
    
    for i in range(1, n):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            if count == cows:
                return True
    return False

def findMaxMinDistance(stalls, n, cows):
    stalls.sort()  # Step 1: Sort the stall positions
    
    # Step 2: Binary search on the answer
    left = 0
    right = stalls[-1] - stalls[0]
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if canPlaceCows(stalls, n, cows, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result