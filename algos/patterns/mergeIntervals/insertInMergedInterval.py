# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Example 2:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
# Example 3:

# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

class Intervals:
    def __init__(self, _start, _end ):
        self.start = _start
        self.end = _end

def insert(intervals, new_interval):
    merged = []
    intervals.append(new_interval)
    intervals.sort(key= lambda x:x[0])
    # merged = intervals
    if len(intervals) < 2:
        return intervals

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            end = max(interval[1], end)
        else:
            merged.append([start, end])
            start = interval[0]
            end = interval[1]

    merged.append([start, end])
    return merged


if __name__ == '__main__':
    print("Intervals after inserting the new interval: " + str(insert([[1,3], [5,7], [8, 12]], [4,6])))
    print("Intervals after inserting the new interval: " + str(insert([[1,3], [5,7], [8, 12]], [4,10])))
    print("Intervals after inserting the new interval: " + str(insert([[2,3], [5,7]], [1,4])))