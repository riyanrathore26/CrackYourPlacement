import math

class Solution:
    def visiblePoints(self, points, angle, location):
        angles = []
        extra = 0

        # Calculate angles of each point relative to the observer's location
        for point in points:
            dx, dy = point[0] - location[0], point[1] - location[1]
            if dx == 0 and dy == 0:
                extra += 1
            else:
                angles.append(math.degrees(math.atan2(dy, dx)))
        # Sort the angles
        angles.sort()
        
        # Duplicate the list to handle the wrapping around of 360 degrees
        angles += [x + 360 for x in angles]

        # Sliding window to find the maximum number of angles within the viewing angle
        max_visible = 0
        left = 0

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra
