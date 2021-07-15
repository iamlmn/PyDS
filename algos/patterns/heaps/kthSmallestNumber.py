# Given an unsorted array of numbers, find Kth smallest number in it.

# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

# Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

# Example 1:

# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
# Example 2:

# Input: [1, 5, 12, 2, 11, 5], K = 4
# Output: 5
# Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].
# Example 3:

# Input: [5, 12, 11, -1, 12], K = 3
# Output: 11
# Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

from heapq import *

def findKth_smallest_number(nums, k):
    '''
    TC: Klog(k) + (N-K)log(k) = NLog(k)
    SC: O(K)
    '''
    minHeap = []
    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] >= minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return minHeap[0]

if __name__ == '__main__':
    nums1 = [1, 5, 12, 2, 11, 5]
    k1 = 3

    nums2 = [1, 5, 12, 2, 11, 5]
    k2 = 4

    nums3 = [5, 12, 11, -1, 12]

    print("Kth smallest number is :" + str(findKth_smallest_number(nums1, k1)))
    print("Kth smallest number is :" + str(findKth_smallest_number(nums2, k2)))
    print("Kth smallest number is :" + str(findKth_smallest_number(nums3, k1)))