# # Kth Largest Number in a Stream

# Problem Statement #
# Design a class to efficiently find the Kth largest element in a stream of numbers.

# The class should have the following two things:

# The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
# The class should expose a function add(int num) which will store the given number and return the Kth largest number.
# Example 1:

# Input: [3, 1, 5, 12, 2, 11], K = 4
# 1. Calling add(6) should return '5'.
# 2. Calling add(13) should return '6'.
# 2. Calling add(4) should still return '6'.
from heapq import *
class KthLargetNumberInStream:
    '''
    Time Complexity : O(Logk)
    Space : O(k)
    '''
    def __init__(self, nums, k):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)


    def add(self, num):
        heappush(self.minHeap, num)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]


if __name__ == '__main__':
    k = KthLargetNumberInStream([3,1,5,12,2,11], 4)
    print("4th largest number is : " + str(k.add(6)))
    print("4th largest number is : " + str(k.add(13)))
    print("4th largest number is : " + str(k.add(4)))