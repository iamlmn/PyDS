# Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

# Example 1:

# Input: points = [[1,2],[1,3]], K = 1
# Output: [[1,2]]
# Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
# The Euclidean distance between (1, 3) and the origin is sqrt(10).
# Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
# Example 2:

# Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
# Output: [[1, 3], [2, -1]]

import math
from heapq import *
class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + "," + str(self.y) + "]" , end="")
    
def find_distance(x,y):
    return abs(math.sqrt((x*x) + (y*y))) 


def find_closest_points(points, k):
    maxHeap = []
    j = 0
    for i in range(k):
        d = find_distance(points[i].x, points[i].y)
        heappush(maxHeap, (-d, points[i]) )

    for i in range(k, len(points)):
        d = find_distance(points[i].x, points[i].y)
        print(d, maxHeap[0][0])
        if d > maxHeap[0][0]:
            heappop(maxHeap)
            heappush(maxHeap, (-d, points[i]) )

    return maxHeap


if __name__ == '__main__':

    result = find_closest_points([Points(1,3), Points(3,4), Points(2, -1)], 2)
    print("Here are the k points closest to the origin.", result)
    
    for d, point in result:
        print([point.x, point.y])

