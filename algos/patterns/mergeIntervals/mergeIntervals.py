class Interval:
    def __init__(self, start, end):
        self.start = start 
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):

    if len(intervals) < 2:
        return intervals
    merged = []

    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval.start <= end:
            end = max(interval.end, end)
        else: #non over lapping interval, add the previous interval and reset
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return merged

if __name__ == '__main__':
    print("Merged intervals: ", end='')
    for i in merge([Interval(1,4), Interval(2,5), Interval(7,9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6,7), Interval(2,4), Interval(5,9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1,4), Interval(2,6), Interval(3,5)]):
        i.print_interval()
    print()