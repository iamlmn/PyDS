# Design a class to calculate the median of a number stream. The class should have the following two methods:

# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

# Example 1:

# 1. insertNum(3)
# 2. insertNum(1)
# 3. findMedian() -> output: 2
# 4. insertNum(5)
# 5. findMedian() -> output: 3
# 6. insertNum(4)
# 7. findMedian() -> output: 3.5
from heapq import *
class MedianOfAStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []


    def insert_num(self, num):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        # Balance
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))


    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2.0
        return -self.maxHeap[0]* 1.0

if __name__ == '__main__':
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is :" + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is :" + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is :" + str(medianOfAStream.find_median()))